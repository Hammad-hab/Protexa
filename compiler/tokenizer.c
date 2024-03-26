/**
 * TODO: implement base tokenizer
*/
#define MAX_TOKENS 10

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "types.c"
#include<stdbool.h>

char ctype(char character) {
    if (character == '&') return 'e';
    else if (character == '{' || character == '}') return 'b';
    else if (character == '[' || character == ']') return 'v';
    else return 'a';
}

void tokenize(char* contents, struct Token output[MAX_TOKENS]) {
    int read_head = 0;
    int write_head = 0;
    while (write_head < (strlen(contents)) && contents[read_head] != '\0') {
        char character = contents[read_head];
        struct Token s1;
        // s1.value[0] = '\0';

        if (ctype(character) == 'e') {
            s1.value = "&";
            strcpy(s1.type, "Element");
            output[write_head] = s1;
            write_head += 1;
        } else if (ctype(character) == 'b') {
            s1.value = character == '{' ? "{" : "}";
            strcpy(s1.type, "Bracket");
            output[write_head] = s1;
            write_head += 1;
        } else if (ctype(character) == 'v') {
            s1.value = character == '[' ? "[" : "]";
            strcpy(s1.type, "Attribute");
            output[write_head] = s1;
            write_head += 1;
        } 
        else {
            if (ctype(contents[read_head + 1]) == 'a') {
                /**
                 * FIXME: Bug with lengthy string
                */
                printf("Here");
                read_head += 1;
                // s1.value = &character;
                char internalCharacter = contents[read_head];
                char* value = &internalCharacter;
                while (internalCharacter != ' ' && contents[read_head] != '\0' && ctype(internalCharacter) == 'a')
                {
                    /* code */
                    internalCharacter = contents[read_head];
                    strcat(value, &internalCharacter);
                    read_head ++;
                    write_head ++ ;
                }
                // printf("%s", value);
                s1.value = value;
                strcpy(s1.type, "AttribV");
                // strcpy(s1.value, value);
                output[write_head] = s1;
                write_head += 1;
                continue;
            } 
            else {
                /**
                 * FIXME: Bug with string parsing
                */
            }
        }
        
        read_head += 1;
    }
}

int main() {
    struct Token output[10];
    char* contents = "&[f]{}";
    tokenize(contents, output);
    for (int i = 0; i < MAX_TOKENS; i++) {
        // if (output[i].value[0] == '\0') break;
        printf("%s:%s\n", output[i].type, output[i].value);
    }
    return 0;
}