#ifndef LOG_C
    #define LOG_C
    #define YELLOW "\033[33m"
    #define RED "\033[31"

    #include<stdio.h>
    #include<string.h>
    #include<errno.h>

    void raiseError(const char* error) {
        printf("\033[31%s\033[0m", error);
        exit(-1);
    }

    void raiseWarning(const char* warning) {
        printf("\033[33m%s\033[0m", warning);
        exit(-1);
    }

#endif