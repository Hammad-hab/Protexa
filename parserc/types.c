#ifndef TYPES_C
#define TYPES_C

    struct Token {
        char type[10];
        char* value;
    };

    struct Program {
        char name[50];
        char* contents;
    };

#endif