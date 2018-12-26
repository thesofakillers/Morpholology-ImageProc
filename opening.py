'''this modules implements grayscale opening with a flat square structuring 
element of a size 5x5 pixels given an input image and an output image name'''

import sys
import cv2
from dilation import dilate
from erosion import erode

#input: cv2 image; output: opened cv2 image
def opn(image):
    #erosion and dilation are used consecutively and the opened image is retrned
    return dilate(erode(image))

    #erode func deals with unsuccessful image loading

#what to do when the script is run
def main():
    img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #reads source img
    cv2.imwrite(sys.argv[2], opn(img))# writes the opened image

if __name__ == '__main__':
    main()