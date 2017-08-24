#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define is(j) (!memcmp(currentJosh, j, 4))

char * parse(char * code) {
	char * ret = (char *) malloc(4096);

	short int icount = 0;
	short int codePosition = 0;
	unsigned char joshPosition = 0;
	unsigned int codeLen = strlen(code);
	char * currentJosh = (char *) malloc(sizeof(char) * 5);

	while (codePosition < codeLen) {
		char cc = code[codePosition++];
		if (!(cc == ' ' || cc == '\t' || cc == '\n')) {
			currentJosh[joshPosition++] = cc;
		}
		if (joshPosition == 4) {
			joshPosition = 0;
			if is("JOSH") {
				ret[icount++] = '+';
			} else if is("josh") {
				ret[icount++] = '-';
			} else if is("Josh") {
				ret[icount++] = '*';
			} else if is("josH") {
				ret[icount++] = '/';
			} else if is("JOsh") {
				ret[icount++] = 'p';
			} else if is("joSH") {
				ret[icount++] = 'g';
			} else {
				printf("Error in parsing!");
			}
		}
	}
	ret[icount] = 'e';

	free(currentJosh);

	return ret;
}

char runCode(char * code) {
	char val = 0;
	short instructionPointer = 0;
	short codeLength = strlen(code);
	char doBreak = 0;
	while (instructionPointer < codeLength) {
		char instruction = code[instructionPointer++];
		switch (instruction) {
		case '+':
			val += 1;
			break;
		case '*':
			val *= 2;
			break;
		case '/':
			val /= 2;
			break;
		case '-':
			val -= 1;
			break;
		case 'p':
			printf("%c", val);
			break;
		case 'g':
			val = getchar();
			break;
		case 'e':
			doBreak = 1;
		}
		if (doBreak) {
			break;
		}
	}
	return val;
}

int main(void) {
	char * code = (char *) malloc(4096);
	gets(code);
	runCode(parse(code));
	return 0;
}
