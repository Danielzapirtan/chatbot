#include <stdio.h>

int main(void) {
	char question[4096];
	char *p = question;
	while (!feof(stdin)) {
		(*p++) = getchar();
	}
	(*p) = 0;
	printf("Curat %s, coane Fanica!\n", question);
	fflush(stdout);
}

