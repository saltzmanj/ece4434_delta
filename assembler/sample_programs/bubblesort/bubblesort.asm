-- Bubblesort Algorithm
[WORD] 32, 1
[FILL] 0x0000, 16

[WORD] 0x000a, 1 ; Array size: 16
[WORD] 0x0000, 1 ; Array base address: 17
[WORD] 0x0002, 1 
[WORD] 0x0007, 1
[WORD] 0x0005, 1
[WORD] 0x0008, 1
[WORD] 0x0003, 1
[WORD] 0x0001, 1
[WORD] 0x0006, 1
[WORD] 0x0009, 1
[WORD] 0x0004, 1

[FILL] 0x0000, 32

; Register: 
;  R6: outer loop counter (i) (size -> 0)
;  R7: inner loop counter (j) (0 -> i - 1)

lil rax, 16
lil rsi, 17 ; Base address of the array
lil r10, 0  ; constant zero
lil r11, 1  ; constant 1

ld r6, rax, 0	; Load array size into r6 ( i = LENGTH ) 0x36

or r6, r6 		; basically a comparison (<- outer loop target)
bz 21				; If i is zero, branch out of the outer loop (i > 0)
lil r7, 0 		; (j = 0) (<- inner loop init)
mov r8, r6 		; (<- inner loop target)
sub r8, r11 	; r8 = i - 1
sub r8, r7 		; i-1 - j
bz 	14			; if j = i - 1, exit inner loop
				; TODO: Calculate branch addresses
				; Main swap logic
mov rdi, rsi
add rdi, r7
ld rcx, rdi, 0 ; Load mem[j] = rcx, mem[j+1] = rdx
ld rdx, rdi, 1
mov r9, rcx
mov r10, rdx
sub r9, r10
; If r9 - r10 <= 0 (e.g. we don't need to swap), branch over swap logic
bn 4			; branch over swap logic (to the add)
st rcx, rdi, 1
sub r8, r11
st rdx, rdi, 0

add r7, r11 ; add 1 to j (j++)
br -16; go back to inner loop start
sub r6, r11 ; Subtract 1 from i (i--)
br -21; go back to outer loop start
nop