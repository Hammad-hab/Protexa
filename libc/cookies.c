#include<stdio.h>
#include<string.h>
#include "log.c"

#ifndef MAX_COOKIE_STORAGE
    #define MAX_COOKIE_STORAGE 100
    #define MAX_COOKIE_LENGTH 150
#endif
#ifndef COOKIE_PATH
    #define COOKIE_PATH "/usr/local/cookies.list"
    #define MAX_WRITE_LIMIT 100
#endif
#ifndef STATUSES
    #define NOTFOUND -0
#endif

static char* cookies[MAX_COOKIE_STORAGE];
static char* cookies_name[MAX_COOKIE_STORAGE];
static int wr_index = 0;


int ArrayIndexOf(const char* array, char* instance) {
    int length = sizeof(array) / sizeof(array[0]);
    for (size_t i = 0; i < length; i++)
    {
        if (array[i] == instance) return i;
        else continue;
    }
    return NOTFOUND;
}

void cookieWriteIndex(char* name, char* value, int index) {
    if (index > MAX_COOKIE_STORAGE) {
        raiseError("Maximumn cookie storage exceeded!");
    }
    strcpy(cookies[index], value);
    strcpy(cookies_name[index], name);
}

void cookieWrite(char* name, char* value) {
    if (wr_index > MAX_COOKIE_STORAGE) {
        raiseError("Maximumn cookie storage exceeded!");
    }
    strcpy(cookies[wr_index], value);
    strcpy(cookies_name[wr_index], name);
    wr_index += 1;
    raiseWarning("PROTEXA_LIB_C: Using cookieWrite can can lead to unexpected results");
}


char* cookieReadIndex(int index) {
    return cookies[index];
}

char* cookieReadName(char* name) {
    int index = ArrayIndexOf(cookies_name, name);
    return cookies[index];
}

void cookieDeleteIndex(int index) {
    raiseWarning("PROTEXA_LIB_C: Cookies are stored in static memory, attempting to delete them will result in memory leaks!");
    cookies[index] = NULL;
}

void cookieExport() 
{
    FILE * file = fopen(COOKIE_PATH, "w");
    char contents[MAX_COOKIE_STORAGE * MAX_COOKIE_LENGTH];
    contents[0] = '\0';
    for (size_t i = 0; i < MAX_COOKIE_STORAGE; i++)
    {
        strncat(contents, cookies_name[i], MAX_COOKIE_LENGTH - strlen(cookies_name[i]) - 1);
        strncat(contents, cookies[i], MAX_COOKIE_LENGTH - strlen(cookies[i]) - 1);
    }
    fprintf(file, "%s", contents);
    fclose(file);
}


