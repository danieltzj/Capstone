to compile file, run 

g++ -L/home/pi/Documents/raspicam-0.1.6/build/src -lraspicam program.cpp -o program -pthread

g++ tells you you are compiling it c++ style, 
program.cpp is source file,
-o program says what you want the output name to be
-pthread says you will be using threads