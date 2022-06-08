commandLauncher: commandLauncher.o
	g++ commandLauncher.o -o commandLauncher

commandLauncher.o: commandLauncher.c
	g++ -c commandLauncher.c

clean:
	rm *.o commandLauncher