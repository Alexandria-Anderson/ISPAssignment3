import numpy as np
import scipy as sp
import skimage.io as io
import matplotlib.pyplot as plt

#should the nef or jpeg image file be used?
def main():

    # creating the tiff file from the .jpeg
    imagePath = 'Desktop/590/baby.jpeg' 
    outputPath = 'Desktop/590/baby.tiff'
    jpegImage = io.imread(imagePath)

    io.imsave(outputPath, jpegImage)

    image = io.imread(outputPath)

    #finding black and white
    black = np.min(image)
    white = np.max(image)

    #finding the rgb values
    rScale = np.max(image[:, :, 0]) - np.min(image[:, :, 0])
    gScale = np.max(image[:, :, 1]) - np.min(image[:, :, 1])
    bScale = np.max(image[:, :, 2]) - np.min(image[:, :, 2])


    #image deminsions
    height, width = image.shape[:2]

    #bits per pixel
    bitsPerPixel = image.dtype.itemsize * 8

    #converting to a dp array
    dpArray = image.astype(np.float64)

    print("black: ", black)
    print("white: ", white)
    print("R scale: ", rScale)
    print("G scale: ", gScale)
    print("B scale: ", bScale)
    print("Bits per pixel:", bitsPerPixel)
    print("Width:", width)
    print("Height:", height)
    
pass

if __name__ == "__main__":
    main()
