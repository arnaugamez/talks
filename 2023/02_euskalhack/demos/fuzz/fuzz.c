#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stuff(char *data, long fsize) {
    for (size_t i = 0; i < fsize; i++) {
        if (data[i] == ('F' ^ i)) return i+1;
    }

    if (*(int*)data != 0xfa1afe1) return 0;

    return (int)(0x1337/(fsize - 10));
}

int main(int argc, char* argv[]) {
    if (argc != 2) return -1;

    FILE *f = fopen(argv[1], "rb");

    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);

    fseek(f, 0, SEEK_SET);
    char *data = malloc(fsize + 1);
    fread(data, 1, fsize, f);
    fclose(f);

    int r = stuff(data, fsize);

}