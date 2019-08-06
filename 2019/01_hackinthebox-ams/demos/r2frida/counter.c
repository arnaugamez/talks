#include <stdio.h>
#include <unistd.h>

int main() {
	int x = 0;
	while(1) {
		printf("%d HITBAMS2019\n", x);
		sleep(1);
		x++;
	}
	return 0;
}
