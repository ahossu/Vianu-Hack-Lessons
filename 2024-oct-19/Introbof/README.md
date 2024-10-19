This is a introductory BOF challenge. 👀 

During the lesson, a server's public IP & port will be given, on which this program (file `main.c`) runs.

You may connect to it using the `nc [ip] [port]` command and exploit this on the server. You can also test this on your own computer (compile it with `gcc main.c -o main -std=c99 -fno-stack-protector -z execstack -no-pie`), but you won't be able to access the flag (it is stored on the server).

**Exploit the program on the server and get the flag!**

**Side quest:** if you have some experience in this type of vulnerabilities (and you easily found the main flag), you should try to gain RCE on the remote server, as there is another vulnerability involved.

The _Linux x86-64 compiled version_ of this program is also given (file `main`), but it is not necesarily needed to solve the main challenge. You might find it helpful for determining the "boffset" when solving the side quest. 😉