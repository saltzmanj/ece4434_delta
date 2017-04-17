0000000000400596 <main>:
# Create stack space  
  400596: 55                    push   rbp
  400597: 48 89 e5              mov    rbp,rsp
  40059a: 48 81 ec b0 01 00 00  sub    rsp,0x1b0

# Stack canary stuff
  4005a1: 64 48 8b 04 25 28 00  mov    rax,QWORD PTR fs:0x28
  4005a8: 00 00 
  4005aa: 48 89 45 f8           mov    QWORD PTR [rbp-0x8],rax
  4005ae: 31 c0                 xor    eax,eax

# Calculate the destination stack address
  4005b0: 48 8d 85 60 fe ff ff  lea    rax,[rbp-0x1a0]

# 0x4007a0: index of the first element in ESI
  4005b7: be a0 07 40 00        mov    esi,0x4007a0

# Move 0x30 (50) into EDX (?)
  4005bc: ba 32 00 00 00        mov    edx,0x32
  4005c1: 48 89 c7              mov    rdi,rax
  4005c4: 48 89 d1              mov    rcx,rdx

# Copy the array (as 50 QWORDS) from .rodata onto the stack
  4005c7: f3 48 a5              rep movs QWORD PTR es:[rdi],QWORD PTR ds:[rsi]

# Initialize the outer loop counter (i): it's in [rbp - 0x1b0]
  4005ca: c7 85 50 fe ff ff 64  mov    DWORD PTR [rbp-0x1b0],0x64
  4005d1: 00 00 00 

# Jump to the outer loop conditional loop exit
  4005d4: e9 93 00 00 00        jmp    40066c <main+0xd6>

# Initialize the inner loop counter (j): It's in [rbp - 0x1ac]  
  4005d9: c7 85 54 fe ff ff 00  mov    DWORD PTR [rbp-0x1ac],0x0
  4005e0: 00 00 00 
# jump to the inner loop comparison
  4005e3: eb 6f                 jmp    400654 <main+0xbe>

# Move j into eax
  4005e5: 8b 85 54 fe ff ff     mov    eax,DWORD PTR [rbp-0x1ac]

# CDQE : sign extend $eax to $rax 
  4005eb: 48 98                 cdqe

# Move item[j] into eax   
  4005ed: 8b 84 85 60 fe ff ff  mov    eax,DWORD PTR [rbp+rax*4-0x1a0]

# Move the item into the i1 = -0x1a8
  4005f4: 89 85 58 fe ff ff     mov    DWORD PTR [rbp-0x1a8],eax

# Move j into eax
  4005fa: 8b 85 54 fe ff ff     mov    eax,DWORD PTR [rbp-0x1ac]
  400600: 83 c0 01              add    eax,0x1

# Now eax = j + 1
  400603: 48 98                 cdqe   # Sign extend j
# Move item[j+1] into eax
  400605: 8b 84 85 60 fe ff ff  mov    eax,DWORD PTR [rbp+rax*4-0x1a0]

# Move item[j+1] into i2 = -0x1a4
  40060c: 89 85 5c fe ff ff     mov    DWORD PTR [rbp-0x1a4],eax
  400612: 8b 85 58 fe ff ff     mov    eax,DWORD PTR [rbp-0x1a8]

# Do the i1 ? i2 comparison
  400618: 3b 85 5c fe ff ff     cmp    eax,DWORD PTR [rbp-0x1a4]

# If i1 < i2 (e.g. items in correct order), skip to loop exit logic
  40061e: 7e 2d                 jle    40064d <main+0xb7>

# Swap logic
# Move j into eax
  400620: 8b 85 54 fe ff ff     mov    eax,DWORD PTR [rbp-0x1ac]
  400626: 48 98                 cdqe   

# Move i2 into edx
  400628: 8b 95 5c fe ff ff     mov    edx,DWORD PTR [rbp-0x1a4]
# Move i2/edx into item[j]
  40062e: 89 94 85 60 fe ff ff  mov    DWORD PTR [rbp+rax*4-0x1a0],edx

# Move j into eax
  400635: 8b 85 54 fe ff ff     mov    eax,DWORD PTR [rbp-0x1ac]
  40063b: 83 c0 01              add    eax,0x1
  40063e: 48 98                 cdqe   

# Move i1 into edx
  400640: 8b 95 58 fe ff ff     mov    edx,DWORD PTR [rbp-0x1a8]
# Move i1/$edx into item[j+1]
  400646: 89 94 85 60 fe ff ff  mov    DWORD PTR [rbp+rax*4-0x1a0],edx

# Add 1 to j (increment inner loop)
  40064d: 83 85 54 fe ff ff 01  add    DWORD PTR [rbp-0x1ac],0x1

# Inner loop breakout
# Subtract one from the outer loop counter and compare
#   that to the inner loop counter (e.g. i < j - 1), although
#   this is translated to exit if i > j - 1

# calculate i - 1
  400654: 8b 85 50 fe ff ff     mov    eax,DWORD PTR [rbp-0x1b0]
  40065a: 83 e8 01              sub    eax,0x1

# Break out of the inner loop if j - i - 1 > 0 (e.g j > i + 1)
  40065d: 3b 85 54 fe ff ff     cmp    eax,DWORD PTR [rbp-0x1ac]
  400663: 7f 80                 jg     4005e5 <main+0x4f>

# Outer loop breakout
# Subtract one from i (outer loop counter)
  400665: 83 ad 50 fe ff ff 01  sub    DWORD PTR [rbp-0x1b0],0x1

# Compare the outer loop (i) value; iterate if i > 0
  40066c: 83 bd 50 fe ff ff 00  cmp    DWORD PTR [rbp-0x1b0],0x0
  400673: 0f 8f 60 ff ff ff     jg     4005d9 <main+0x43>

# Print the list

# Else, zero it out and proceed
  400679: c7 85 50 fe ff ff 00  mov    DWORD PTR [rbp-0x1b0],0x0
  400680: 00 00 00 
  400683: eb 27                 jmp    4006ac <main+0x116>
  400685: 8b 85 50 fe ff ff     mov    eax,DWORD PTR [rbp-0x1b0]
  40068b: 48 98                 cdqe   

# Pointer to the sorted list
  40068d: 8b 84 85 60 fe ff ff  mov    eax,DWORD PTR [rbp+rax*4-0x1a0]
  400694: 89 c6                 mov    esi,eax

# First printf argument: format string
  400696: bf 80 07 40 00        mov    edi,0x400780
  40069b: b8 00 00 00 00        mov    eax,0x0
  4006a0: e8 cb fd ff ff        call   400470 <printf@plt>
  4006a5: 83 85 50 fe ff ff 01  add    DWORD PTR [rbp-0x1b0],0x1
  4006ac: 83 bd 50 fe ff ff 63  cmp    DWORD PTR [rbp-0x1b0],0x63
  4006b3: 7e d0                 jle    400685 <main+0xef>
  4006b5: b8 00 00 00 00        mov    eax,0x0
  4006ba: 48 8b 4d f8           mov    rcx,QWORD PTR [rbp-0x8]
  4006be: 64 48 33 0c 25 28 00  xor    rcx,QWORD PTR fs:0x28
  4006c5: 00 00 
  4006c7: 74 05                 je     4006ce <main+0x138>
  4006c9: e8 92 fd ff ff        call   400460 <__stack_chk_fail@plt>
  4006ce: c9                    leave  
  4006cf: c3                    ret  