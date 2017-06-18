#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	FILE *fp;
	char s[256];

	if((fp=fopen("memoca.txt", "w+")) == NULL){
		perror("fopen");
		exit(EXIT_FAILURE);
	}

	while(fgets(s, 256, fp) != NULL){

		printf("%s", s);

	}
	printf("input end\n");
	fputs("test input3\n", fp);
	fputs("test input2\n", fp);

	fclose(fp);

	return 0;

}

