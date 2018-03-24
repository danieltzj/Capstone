#include <iostream>
#include <ctime>
#include <unistd.h>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <thread>
#include <raspicam/raspicam.h>

using namespace std;

//set paths for where the latest picture and translated text files are stored
string latest_picture = "../pictures/latest_picture.ppm";
string latest_translation = "../translated_text/latest_translation";

//function to convert picture to text; pass in image location
//by default, uses latest picture and translation location (cannot use this feature for threads)
void picture2text(string image_src = latest_picture, string text_output = latest_translation);

int main(int argc, char **argv)
{
	raspicam::RaspiCam Camera; //Camera Object

	//Open the Camera
	cout <<"Opening Camera..." <<endl;
	if ( !Camera.open())
	{
		cerr << "Error opening camera" <<endl;
		return -1;
	}

	// wait until camera stabilizes
	cout << "Sleeping for 3 secs" << endl;
	usleep(3000000);

	cout << "type 'stop' to stop the program" << endl;
	char str;

	do
	{
		str = getchar();

		Camera.grab();

		// allocate memory
		unsigned char *data=new unsigned char[  Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB )];

		//extract the image in rgb format
		Camera.retrieve ( data );//get camera image

		//save
		std::ofstream outFile ( latest_picture,std::ios::binary );
		outFile<<"P6\n"<<Camera.getWidth() <<" "<<Camera.getHeight() <<" 255\n";
		outFile.write ( ( char* ) data, Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB ) );
		cout<<"Image saved at raspicam_image.ppm"<<endl;
		//free resrources    
		delete data;

		thread translate_picture(picture2text, latest_picture, latest_translation);
		translate_picture.join();
	}while(str != '\n');

	return 0;
}

void picture2text(string image_src, string text_output)
{
	system(("tesseract " + image_src + " " + text_output ).c_str());
}