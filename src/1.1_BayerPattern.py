import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt
import rawpy

def identify_bayer_pattern(image_path):
    image = io.imread(image_path)
    image = image.astype(np.uint8)
    
    grayscale_image = color.rgb2gray(image)
    plt.imshow(grayscale_image, cmap='gray')
    plt.show()

    
    red_channel = grayscale_image[::2, ::2]
    green_channel1 = grayscale_image[1::2, ::2]
    green_channel2 = grayscale_image[::2, 1::2]
    blue_channel = grayscale_image[1::2, 1::2]
    
    red_mean = np.mean(red_channel)
    green_mean1 = np.mean(green_channel1)
    green_mean2 = np.mean(green_channel2)
    blue_mean = np.mean(blue_channel)
    
    if green_mean1 > green_mean2:
        if red_mean > blue_mean:
            return "RGGB"
        else:
            return "GRBG"
    else:
        if red_mean > blue_mean:
            return "GBRG"
        else:
            return "BGGR"

image_path = "data\\baby.jpeg"
bayer_pattern = identify_bayer_pattern(image_path)
print("Bayer pattern:", bayer_pattern)

image_path_raw = "data\\baby.nef"

def get_bayer_pattern(raw_file):
    with rawpy.imread(raw_file) as raw:
        BayerPattern = raw.raw_pattern
        bayer_partten = "".join([chr(raw.color_desc[i]) for i in raw.raw_pattern.flatten()])

    return BayerPattern, bayer_partten

print(get_bayer_pattern(image_path_raw))

