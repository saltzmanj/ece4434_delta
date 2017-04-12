# ECE4435 - Enhanced Assembler

## Authors
Jonathan Lowe (@jl4ge) and Jake Saltzman (@saltzmanj)

## User Guide

### Calling the Assembler

The assembler accepts the file to be assembled as a command line argument and outputs to `stdout`. Call like so:

```
sh$ ./main.py input_file.asm > memoryinit.txt
```


### Syntax

The assembler uses the syntax specified by the [ECE 4435 ISA](https://github.com/saltzmanj/ece4434_delta/blob/master/assembler/ISA4435.pdf). Registers are specified R0, R1, ..., R15. All  numeric literals except where noted can be specified as either signed or unsigned decimal or hexidecimal. Like VHDL, everything is case insensitive and comments are declared with `--`. Newlines are ignored.

Here's some sample code to get a feel for it.

```
-- Perform a*b via repeated addition of b
[WORD] 0x0000, 1
[WORD] 0x0004, 1 -- Memory location of a, 0x0001
[WORD] 0x0006, 1 -- Memory location of b, 0x0002
[WORD] 0x0000, 1 -- Memory location of a*b, after algorithm, 0x0003
[FILL] 0xFFFF, 16 -- Fill up to address 16

LIL R15, 0x01 	-- Use R15 as base register; this is address 16
LIL R2, 0x01 	-- R2 const 1
LIL R4, 0x00 	-- R4 as accumulator

LD R5, R15, 0x01 -- Load b into R5

ADD R4, R4 		-- Accumulate
SUB R5, R2 		-- Subtract 1 from R5
BZ 2 			-- Branch to end if we're done
BR -3			-- otherwise, branch back to the add

ST R4, R15, 0x02 -- Store the result in memory

```

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


