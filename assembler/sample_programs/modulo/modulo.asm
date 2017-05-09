[WORD] 0x0008, 1
[FILL] 0x0008, 8

lil r0, 0
lil r1, 1
lil r2, 0
lih r2, 0x80

lil r3, 0xfe
lil r4, 0x30
lih r4, 0

lil r14, 0x18
lil r5, 0x10

ld r6, r4, 0
ld r7, r4, 1
ld r8, r4, 2

add r6, r0
bz 0x12

mov r9, r6
sub r9, r7

bn 0x0f
rl r8, r8
and r8, r3
rl r7, r7
bc 0x04

mov r9, r7
sub r9, r6

bn 0x03
sub r7, r6

add r8, r1
sub r5, r1
bz 0x2
jmp r14, 1

st r7, r4, 3
st r8, r4, 4

nop
br -1
[FILL] 0x0000, 0x30
[WORD] 0x0010, 1
[WORD] 0x0000, 1
[WORD] 0x0100, 1

[WORD] 0xFFFF, 1
[WORD] 0xFFFF, 1

[FILL] 0x0000, 0x64