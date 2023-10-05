global _start

section .text

_start:
    mov rax, 123
    add rax, rsi
    xor rax, rdi
    mov rbx, 0x2
    add rax, rbx
    mov rdi, 0x3
    mov rsi, rax
    add rax, rbx
    xor rax, rdi
    mov rbx, 0x7
    and rax, rbx
    mov rdi, 1336
    add rax, rdi
    cmp rax, 1337
    jnz bad

good:
    xor rdi, rdi
    jmp exit
    
bad:
    mov rdi, 1

exit:
    mov rax, 0x3c
    syscall