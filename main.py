from PIL import ImageDraw, ImageFont, Image
import cv2
import numpy as np
import math

def get_data(mode):
    Font = ImageFont.truetype("C:\Windows\Fonts\STXINGKA.ttf", 20)
    scale = 0.1
    char_list = Character[mode]
    return char_list, Font, scale

def get_char(i):
    return char_list[math.floor(i * interval)]

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

# Getting the character List, Font and Scaling characters for square Pixels
char_list, Font, scale = get_data("complex")
charlen = len(char_list)
interval = charlen / 256

# setting the size of chars( use to change the frame size)
charwidth, charheight = 8, 8

# Taking the video as input(replace the filename with the input video)
fileName = "naruto.mp4"
cap = cv2.VideoCapture(fileName)

while True:

    # Taking frames from the video
    _, img = cap.read()
    img = Image.fromarray(img)

    # resizing height and width of input frames
    img_width, img_height = img.size
    img = img.resize((int(scale * img_width), int(scale * img_height * (charwidth / charheight))), Image.NEAREST)
    img_width, img_height = img.size
    pixel = img.load()

    # Calculating height and width of the output frames
    output_width = charwidth * img_width
    output_height = charheight * img_height

    # creating output frames
    outputImage = Image.new("RGB", (output_width, output_height), color=(0, 0, 0))
    dest = ImageDraw.Draw(outputImage)

    # Mapping the characters
    for i in range(img_height):
        for j in range(img_width):
            r, g, b = pixel[j, i]
            h = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixel[j, i] = (h, h, h)
            dest.text((j * charwidth, i * charheight), get_char(h), font=Font, fill=(r, g, b))

    open_cv_image = np.array(outputImage)

    # wait time of every frame(use to change the speed of the video)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    cv2.imshow("output video", open_cv_image)

cap.release()
cv2.destroyAllWindows()