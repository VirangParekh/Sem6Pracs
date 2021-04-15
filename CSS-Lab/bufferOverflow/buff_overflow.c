#include <string.h>
#include <stdio.h>

void func(char *str)
{
    char bufer[1024];
    strcpy(bufer, str);
}

int main(int argc, char *argv[])
{
    char aaa[500];
    func(argv[1]);
    return 0;
}
