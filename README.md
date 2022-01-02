# Background Color Affect on AI
Tests to figure out which of 4 colors used in training is best for identifying on other colors

# Recreating the Experiment

## Positioning

Using the [Microsoft Studio Webcam](https://www.microsoft.com/en-us/d/lifecam-studio/91dt6wmfdlb3), and a Ring Light positioned as follows 

Ring Light 29 in Above tile (Centered)

Camera 5in to the right of the tile facing straight down

## Capturing Pictures

### Installing dependencies

The picture script requires you to have both python and the python module `Open CV` installed
To install opencv just run `pip install opencv-python` after installing python 3.10 from https://www.python.org/downloads/

### Emptying the folders

Make sure in the images folder the folders with color names are empty

### Runing the script

Following the positioning stated above capture your pictures using [This Script](https://github.com/Heppcat-Programming/background-color-ai-tests/blob/main/pictures.py) to run the script while in the same folder as it run `python pictures.py` it will take a picture every 30 seconds when you are ready press `p` to start and follow the instructions in the terminal.

## Labeling the images

First install the dependencies using `pip install pyqt5 lxml`

Go to the folder named `labelimg` and run `python labelImg.py` then using the buttons on the side open the folder with the first image. Then press w and make the selection. After doing that save the image and go on to the next one. To copy the selection from image to image press `Ctrl + V`, but you have to reselect the object for each background color.


## Training
### Repeat Per Color
    Create a mobilenet model with 12 of the labeled images (from that color)

## Testing
    Test the models using all of the remaining 3 images from every color 