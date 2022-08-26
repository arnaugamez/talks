#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
  uint8_t x, y, z;
  x = (uint8_t) atoi (argv[1]);
  y = (uint8_t) atoi (argv[2]);

  z = x ^ y;

  printf("z = %d\n", z);
  return 0;
}
