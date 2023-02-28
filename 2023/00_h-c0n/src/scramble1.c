#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

uint64_t scramble(uint64_t x, uint64_t y) {
    return (x | y) + (x ^ y);
}

int main() {
    printf("Result %" PRIu64 "\n", scramble(1234,5678));
    return 0;
}