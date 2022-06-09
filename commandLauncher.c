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
	char* args[argc] = {0};
	for(int i = 0; i < argc; i++){
		args[i] = argv[i+1];
	}
	launchProcesses(args);
	
}

int launchProcesses(char* proc[]){
	char* argPtr = proc[0];
	int i = 0;
	while(argPtr != NULL){
		proc[i] = strdup(proc[i]);
		argPtr = proc[++i];
	}
	int rc = fork();
	if (rc<0){
		fprintf(stderr, "fork failed\n");
		return -1;
	}
	else if (rc == 0){
		execvp(proc[0], proc);
	}
	else{
		int wc = wait(NULL);
		printf("I am parent of %d (wc:%d) (pid:%d)\n", rc, wc, (int) getpid());
	}
	return 0;
}