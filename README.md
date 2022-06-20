# Asciify: ASCII Art Generator

## Project Description :

ASCII (American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
Other than texts, we can use this for images and videos. So here we are dividing the video into numerous frames and then converting every frame into ascii art. Then presenting them one by one to make it look like a video.

## How to run the project: include all the dependencies :
• First we need to install necessary libraries – **OpenCV**, 
**PIL(python image library)**, 
**Numpy**, 
**Math**.

• Take Input (.mp4) video file for ASCII video creation.

• Rename “**filename**”  as the input file directory.

• Use “**Font**” from the default windows fonts folder (.ttf file).
  
    E.g Font = ImageFont.truetype("C:\Windows\Fonts\STXINGKA.ttf", 20)

• Specify the **char_list** to be used from the character list.
	
    i.e. char_list = Character["mode"]  mode can be “standard” or “complex”.

• Setting **charwidth, charheight and scale**.

## Internal working of a project :
• First, we will take the input video from the project directory. Then we will select a character list for mapping our output frames, also we will be setting the character dimensions to fit our output frame.

• After this, we will resize the input frames that we have extracted from the source video file, then we will calculate height and width of the output frame with respect to the input frames and character size.

• Then  we will be mapping the output frame through rows and columns. After that, we will fill the output frame with assigned characters using the **ImageDraw.draw()** function, then we will display every frame with some time lag using **cv2.waitkey()**.

• We can use the **cv2.waitkey()** function to change the speed of the video.

## Learning takeaways from the project :
• Work experience on the project-based libraries/frameworks like **OpenCV, PIL(python image library), numpy**.

• Understood the basis of image processing.

• Using image processing to convert videos into ascii art.

• Better understanding of the python language.

## Resources/references used during working on the project :

•	https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles

•	https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/

•	https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

•	https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html

•	https://pillow.readthedocs.io/en/stable/reference/Image.html
