
// this shall be compiled with the following command:
// gcc main.c -o main -std=c99 -fno-stack-protector -z execstack -no-pie
#include <stdio.h>

int main() {
    while(1) {
        int x = 0;
        char name[32]="";
        printf("What's your name? ");
        fflush(stdout); 
        
        gets(name);    

        if(x) {
            break;
        } 

        printf("Hello, ");
        printf(name);
        printf("!\n");
        fflush(stdout);
    }

    // You pwned it! Here's your flag (read from a file): VianuCTF{...} 
    FILE *fptr = fopen("flag", "r");
    char flag[35]; 
    fgets(flag, 35, fptr);
    printf("Congrats! You bypassed it!\nHere's your flag: %s\n", flag);
    fflush(stdout);
    return 0;
}