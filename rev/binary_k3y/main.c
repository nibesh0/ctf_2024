#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define CFT "rabithole"


int randomInteger(int min, int max) {
    return min + rand() % (max - min + 1);
}

int A(const char *c, char **output) {
    if (c == NULL || output == NULL) {
        return -1;
    }
    size_t len = strlen(c);
    *output = (char *)malloc(len * 2 + 1);
    if (*output == NULL) {
        return -1;
  
  }

    srand(0); 
    for (size_t j = 0; j < len; j++) {
        int i = randomInteger(0, 50);
        int temp = i ^ (unsigned char)c[j]; 
        sprintf((*output) + j * 2, "%02X", (unsigned char)temp);
    }
    (*output)[len * 2] = '\0'; 

    return 0;} 
int main() {
    printf("Enter the password to encrypt: ");  
    char input[100];
    scanf("%99s", input); 

    char *output = NULL; 
    if (A(input, &output) !=0 ) { 
        printf("Error during encryption.\n");
        return 1; 
    }
   if(strcmp(output,"49654F59731646421E675A7D257D29645441432C5A75")==0)printf("God job, my friend! You did it!");
    
   else  printf("Error!!! Encrypted output (hex): %s\n", output);
       
    free(output); 
    return 0;
}
