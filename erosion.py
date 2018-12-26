'''this modules implements grayscale erosion with a flat square structuring 
element of a size 5x5 pixels given an input image and an output image name'''
import sys
import cv2
import numpy as np

#input: cv2 image; output: greyscale eroded cv2 image
def erode(image):
    #checks if an image file succesfully loaded
    if not image is None:
        
        #allocating an array for the eroded image
        eroded = np.copy(image)
        
        #looping over each pixsel of the array
        for j in range(image.shape[0]):
            for i in range(image.shape[1]):
                
                #the following if statements deal with borders
                #the kernel is simply cut off
                for k in range(2):
                    if (j == k):
                        if (i >= 2):
                            eroded[j][i] = np.amin(image[j-k:j+3, i-2:i+3])
                        elif (i > k):
                            eroded[j][i] = np.amin(image[j-k:j+3, i-(k+1):i+3])
                        elif (i == k):
                            eroded[j][i] = np.amin(image[j-k:j+3, i-k:i+3])
                    if (i == k):
                         if (j >= 2):
                             eroded[j][i] = np.amin(image[j-2:j+3, i-k:i+3])
                         elif (j > k):
                             eroded[j][i] = np.amin(image[j-(k+1):j+3, i-k:i+3])
                         elif (j == k):
                             eroded[j][i] = np.amin(image[j-k:j+3, i-k:i+3])
                            
                #pixels where kernel fits fine
                if (j >= 2 and i >= 2):
                    #sets pixel value to minimum of kernel: erosion
                    eroded[j][i] = np.amin(image[j-2:j+3, i-2: i+3])       
                        
        #returns eroded image               
        return eroded
      
    #lets user know that the image did not load successfully    
    else:
        print("No image file successfully loaded.")
    
#what to do when the script is run
def main():
    img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE) #reads source image
    cv2.imwrite(sys.argv[2], erode(img)) #writes eroded image
    
    
if __name__ == '__main__':
    main()