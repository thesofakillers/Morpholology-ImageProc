# Morphological Image Processing

Originally made for Durham University's Department of Computer Science's course _Software Methodologies_ under the sub-module _Image Processing_, as part of the coursework in 2017/2018.

This repository contains 4 simple scripts able to perform [morphological](https://en.wikipedia.org/wiki/Mathematical_morphology) [closing](https://en.wikipedia.org/wiki/Closing_(morphology)), [opening](https://en.wikipedia.org/wiki/Opening_(morphology)), [dilation](https://en.wikipedia.org/wiki/Dilation_(morphology)) and [erosion](https://en.wikipedia.org/wiki/Closing_(morphology)) on an input PNG image.

## Requirements

This project was made utilizing [Python 2.7](https://www.python.org/download/releases/2.7/).

In addition, please ensure that the following modules are installed:

-   [OpenCV](https://opencv.org/)
-   [NumPy](http://www.numpy.org/)

## Instructions

To perform a morphological operation `<operation>`, on an input image `<input>.png`, in the terminal type

`python <operation>.py <input>.png <output>.png`.

Notice that the desired name of the resulting output image is necessary.
