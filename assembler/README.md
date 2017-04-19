# ECE4435 - Enhanced Assembler / Disassembler

## Authors
Assembler: Jonathan Lowe (@jl4ge) and Jake Saltzman (@saltzmanj)
Disassembler: Jake Saltzman (jss7kj)
## Assembler User Guide

### Calling the Assembler

The assembler accepts the file to be assembled as a command line argument and outputs to `stdout`. Call like so:

```
sh$ ./lexerparser.py input_file.asm > memoryinit.txt
```


### Syntax

The assembler uses the syntax specified by the [ECE 4435 ISA](https://github.com/saltzmanj/ece4434_delta/blob/master/assembler/ISA4435.pdf). Registers are specified R0, R1, ..., R15. All  numeric literals except where noted can be specified as either signed or unsigned decimal or hexidecimal. Like VHDL, everything is case insensitive and comments are declared with `--`. Newlines are ignored.

Here's some sample code to get a feel for it.

```
-- Perform a*b via repeated addition of b
[WORD] 16, 1    -- First line should be the address of the first code instruction
[WORD] 0x0000, 1
[WORD] 0x0004, 1 -- Memory location holding a
[WORD] 0x0006, 1 -- Memory location holding b
[WORD] 0x0000, 1 -- Memory location holding a*b
[FILL] 0xFFFF, 16 -- Fill up to address 16

LIL R15, 0x01 	-- Use R15 as base register
LIL R2, 0x01  	-- R2 const 1

LD R3, R15, 0x01  --Load a into R3
XOR R4, R4 	      -- R4 is accumulator

LD R5, R15, 0x2 -- Load b into R5

ADD R4, R3 		-- Accumulate
SUB R5, R2 		-- Subtract 1 from R5
BZ 2 			    -- Branch to end if we're done
BR -3			    -- otherwise, branch back to the add

ST R4, R15, 0x02 -- Store the result in memory

```

You can also use x86-style register names if you want. The following register names are equivalent:

Register Number|Register Alias
---------------|--------------
R0 | RAX
R1 | RBX
R2 | RCX
R3 | RDX
R4 | RDI
R5 | RSI
R14| RJL\*
R15 | RCT\*\*

\* RJL: jump-and-link register. Calling a JAL will place the return address in this register.

\*\* RCT: Check table register. Holds the base address of the check table: used for the instruction checker module.



### Instructions

**Loads and Stores**
```
LD/ST <DestID>, <BaseRegisterID>, <5bit unsigned offset>

LD R1, R10, 0x04
ST R1, R10, 0x10

ST R1, R10, 0x20 # BAD: offset > 5 bits
```

**Register Transfer**
```
MOV <DestID>, <SrcID>

MOV R2, R1
```

**Load Immediate**
```
LIL/LIH <DestID>, <8bit sign-extended value>

LIL R1, 0xFF
LIH R1, -2
```

**Arithmetic**

```
ADD/ADC/SUB/SBC/AND/OR/NOT/XOR <DestID>, <SrcID>
SL/SRL/SRA/RRA/RR/RL <DestID>, <SrcID>

ADD R1, R2
NOT R1, R3
XOR R1, R1
etc.
```

**Absolute Jump**

```
JMP/JAL <BaseID>, <8bit signed offset >

JMP R1, 0x01
JAL R2, -5
```

**PC Relative Branch**
```
BR/BC/BO/BN/BZ <8-bit signed offset>

BR 0x05

The following two are equivalent:
BO -2
BO 0xFE
```
### Instruction Checking
This ISA supports the instruction check module. 

**CHK Instructions**

Instruction | Description
-------------|---------------
Check Instruction | Activates the instruction checker module for the immediately following instruction by comparing a redundant version of the instruction elsewhere in memory. The address of the redundant instruction is [RCT + <9 bit immediate offset> ].

#### Encoding

Instruction| 15:13 | 12 | 11:9 | 8:0
-----------------------|------|----|------|-----
Check Instruction | 000 | 1 | 000 | Offset into redundancy table

#### Assembly


**Check Instruction**
```
-- Load address of redundancy table
LIL RCT, 0x00
LIH RCT, 0x80

...

CHK INST_CHECK, 0
LD R1, R12, 0x04 -- Example instruction
MOV R5, R1
ADD R1, R5
CHK INST_CHECK, 1
ADD R1, R5

...

-- End of program
[FILL] 0x0000, 0x8000
-- Begin Redundancy table
LD R1, R12, 0x04 -- Redundant Instruction 0
ADD R1, R5 -- Redundant Instruction 1

```

### Pseudo-Instructions

**Literals**

These allow the programmer to insert 16 bit values directly into the output. The syntax is: ```[WORD] <16 bit literal>, <integer repeats>```

For example:
```
[WORD] 0xAAFF, 5
```
will be compiled to 
```
1010101011111111
1010101011111111
1010101011111111
1010101011111111
1010101011111111
```

**Filling**

It is often useful to make the memory a certain size or fill it with values until it is a certain size. While one could use `[WORD]` to accomplish this, you would have to change its `<repeat>` argument any time you added an instruction before it. To remedy this, you can use the `[FILL]` instruction to fill the memory with an arbitrary value up to, but not including, a specific address.

The syntax for `[FILL]` is `[FILL] <16 bit literal>, <max address>`

Here's an example:

```
BZ 2
ST R2, R1, 0x11
ADD R4, R15
[FILL] 0xFFFF, 8
NOP
```

compiles down to

```
1110001000000010
0100010000110001
1010100111100000
1111111111111111
1111111111111111
1111111111111111
1111111111111111
1111111111111111
0000000000000000
```

Note that the NOP is instruction at address 8: `[FILL]` goes up to, but doesn't include, its `<max address>` argument.

## Disassembler: User Guide

### Calling the disassembler

The disassembler has two functions: it can disassemble a binary file, or combine a binary file with a tracefile to produce a view of the memory state after a complete run of the binary file. 

**Disassembly-only mode**
```
sh$ ./memview.py memoryinit.txt
```

This mode disassembles the input binary file, with three columns: address, data, and instruction. The first instruction (0x0000) is interpreted as a jump to the specified address in the data column, as per the ISA. 

Branch target addresses are calculated; the target address is enclosed in angular brackets (e.g. <0x0040>)


```
0x0000  : 0x0002    | (JMP 0x0020)
0x0001  : 0x0000    |
.
.
.
0x0020  : 0x8010    | LIL   rax, 0x10
0x0021  : 0x8A11    | LIL   rsi, 0x11
0x0022  : 0x9400    | LIL   r10, 0x0
0x0023  : 0x9601    | LIL   r11, 0x1
0x0024  : 0x2C00    | LD    r6, rax, 0x0
0x0025  : 0xACC5    | OR    r6, r6
0x0026  : 0xE215    | BZ    21 <0x003B>
0x0027  : 0x8E00    | LIL   r7, 0x0
0x0028  : 0x70C0    | MOV   r8, r6


```

**Disassemble + Trace Mode**
This mode disassebles the input binary file, then parses the tracefile and applies the changes contained within. The output produced by the program shows the value of memory *after* all the writes in the tracefile occur. 