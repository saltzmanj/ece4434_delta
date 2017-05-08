[WORD] 0x0040, 1 ; Address of first instruction 
[FILL] 0x0000, 16

[WORD] 0x2d00, 1 ; Cordic reference angles, address 16
[WORD] 0x1a91, 1
[WORD] 0x0e09, 1
[WORD] 0x0720, 1
[WORD] 0x0394, 1
[WORD] 0x01ca, 1
[WORD] 0x00e5, 1
[WORD] 0x0073, 1
[WORD] 0x0039, 1
[WORD] 0x001d, 1
[WORD] 0x000e, 1
[WORD] 0x0007, 1
[WORD] 0x0004, 1
[WORD] 0x0002, 1
[WORD] 0x0001, 1
[WORD] 0x0000, 1

[FILL] 0x0000, 48
[WORD] 0x0025, 1 ; angle 48
[WORD] 0xFFFF, 1 ; COS : 49
[WORD] 0xFFFF, 1 ; SIN : 50
[WORD] 0x0008, 1 ; MUL_SHIFTS : 51
[WORD] 0x0010, 1 ; CORDIC_NTAB: 52
[WORD] 0x009B, 1  ; CORDIC_GAIN = 155
[FILL] 0x0000, 64

lil r10, 0
lil r11, 1

lil r8, 16 ; R8 = Cordic table base address  
lil r9, 48 ; R9 = constants/params base address

ld rax, r9, 0 ; Load desired angle into rax
ld rcx, r9, 6 ; Initialize x (rcx) to the cordic gain
lil rdx, 0    ; Initialize y (rdx) to 0: 

ld rsi, r9, 3 ; Load number of shifts into rsi

sl rax, rax
sub rsi, r11
bz -2
br 3

ld rsi, r9, 4 ; Load CORDIC_NTAB into rsi (loop max)
lil rdi, 0 ; RDI: loop counter

mov rbx, rdi ; <- Loop target 
sub rbx, rsi
bn * ; if loop over branch out


mov rbx, rax ; 
sub rbx, r10
bn * ;if angle is negative, jump to negative case

ld rbx, r8, 0 ; Load angle[i]
sub rax, rbx
mov r13, rcx ; r13 = xnew
mov r14, rdx ; r14 = ynew

; Calculate y >> i
mov rbx, rdi ; rbx, copy of i

sl r14, r14
sub rbx, 1
bz 2
br 3

add r13, r14
mov rcx, r13  

; Negative case