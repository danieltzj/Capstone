# Simple Makefile for our program

program: program.o
	g++ -L/home/pi/Documents/raspicam-0.1.6/build/src -lraspicam program.cpp -o program -pthread

clean:
	rm *.o program