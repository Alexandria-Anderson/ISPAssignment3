import numpy as np
import scipy as sp
import skimage.io as io
import matplotlib.pyplot as plt

#should the nef or jpeg image file be used?
def main():

    imagePath = 'Desktop/590/baby.tiff' 
    white = 16383
    black = 0

    image = io.imread(imagePath)
    plt.imshow(image)
    plt.show()


    #image deminsions
    height, width = image.shape[:2]

    #bits per pixel
    bitsPerPixel = image.dtype.itemsize * 8

    #converting to a dp array
    dpArray = image.astype(np.float64)

    # scaling factor and shift for linear transformation

    scale_denom = max(white - black, 1e-10)  # Ensure the denominator is not zero
    scale = 1.0 / scale_denom
    shift = -np.float64(black) * np.float64(scale)
    # linear transformation
    imageLinear = dpArray * scale + shift

    # Clip values to range [0, 1]
    imageLinear = np.clip(imageLinear, 0, 1)

    print("Bits per pixel:", bitsPerPixel)
    print("Width:", width)
    print("Height:", height)
    
pass

if __name__ == "__main__":
    main()
