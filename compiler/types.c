#ifndef TYPES_C
#define TYPES_C

    // Defining Constants
    #define MAX_TOKENS 1000 // Maximum amount of empty null tokens a program can parse before exiting
    #define TYPE_NAME_LENGTH 15
    

    // Defining seeType Types
    #define ELEMENT 'e'
    #define BRACKETS 'b'
    #define ATTRIBUTE 'a'
    #define VALUE 'p'
    #define SPACE ' '

    #include<regex.h>
    #include<stdio.h>

    // Defining Types
    typedef char* String;
    typedef char** StringPtr;
    typedef char Str[];
    typedef char Typename[TYPE_NAME_LENGTH];

    const String REGEX_CHARACTER = "[A-Za-Z0-9]";
    struct Token {
        String type;
        String value;
        Str Value;
    };

    struct Program {
        char name[50];
        String contents;
    };

    char seeType(char character) {
        if (character == '&') {
            return ELEMENT;
        } else if (character == '{' || character == '}') {
            return BRACKETS;
        } else if (character == '[' || character == ']') {
            return ATTRIBUTE;
        } else {
            return VALUE;
        }
    }

    void raise(String Error) {
        printf("\033[1;31mPROTEXA_INTERNAL_ERROR:\n\t%s\033[0m", Error);
        exit(-1);
    }

    // int len(char* array) {
    //     int array_length = sizeof(array) / sizeof(array[0]);  
    //     return array_length;
    // }
    
    

#endif