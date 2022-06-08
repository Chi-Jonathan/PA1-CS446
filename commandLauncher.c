#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>

int launchProcesses(char* proc[]);

int main(int argc, char* argv[]){
	printf("hello world (pid:%d)\n", (int) getpid());
	int rc = fork();
	if (rc<0){
		fprintf(stderr, "fork failed\n");
		exit(1);
	}
	else if (rc == 0){
		printf("hello, I am child (pid:%d)\n", (int) getpid());
		/*char *myargs[3];
		myargs[0] = strdup("wc");
		myargs[1] = strdup("p3.c");
		myargs[2] = NULL;
		execvp(myargs[0], myargs);*/
		char* args[argc] = {0};
		for(int i = 0; i < argc; i++){
			args[i] = argv[i+1];
		}
		launchProcesses(args);
		printf("arg1: %s\n", args[0]);
	}
	else{
		int wc = wait(NULL);
		printf("hello, I am parent of %d (wc:%d) (pid:%d)\n", rc, wc, (int) getpid());
	}
}

int launchProcesses(char* proc[]){
	return -1;
}