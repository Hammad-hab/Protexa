#ifndef TYPES_C
#define TYPES_C

    typedef struct {
        char type[10];
        char* value;
    } Token;

    typedef struct {
        char* name;
        char* contents
    } Program;

#endif