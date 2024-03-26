#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "types.c"

int LEX_Element(char character, struct Token output) {
    if (seeType(character) == ELEMENT) {
       return 0;
    }
    return 1;
}

int LEX_Name(char contents[], int read_head, struct Token output) {
    char character = contents[read_head];
    if (seeType(character) == VALUE) {
       Str value = "";
       int index = 0;
       while(read_head < (strlen(contents)) && seeType(contents[read_head]) == VALUE && contents[read_head] != SPACE) {
            value[index] = contents[read_head];
            // strcat(value, &contents[read_head]);
            // value[index] = contents[read_head];
            read_head ++;
            index ++;
       }
       read_head ++;
      //  value[index + 1] = '\0';
      //  strcpy(output.Value, value);
         output.value = value;
         output.type = "Name";

       
       return read_head;
    }
    return -1;
}

int main() {
    printf("hi");
    int index = 1;
    struct Token output1;
    output1.value = "";
    output1.type = "";
    // struct Token output2;

    index = LEX_Name("{Hello World}", index, output1);
    // index = LEX_Name("{Hello World}", index, output2/);
    printf("%s\n", output1.value);
    // printf("%s\n", output2.value);
    return 0;
}