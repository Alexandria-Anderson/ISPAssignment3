import numpy as np
from scipy.interpolate import interp2d
import scipy as sp
import skimage.io as io
import matplotlib.pyplot as plt

image = io.imread('data/baby.jpeg')
image = image.astype(np.uint8)

def demosaic_bilinear(raw_image):

    # Define the new set of x and y coordinates where you want to interpolate
    new_x = np.linspace(0, raw_image.shape[1], 2 * raw_image.shape[1])
    new_y = np.linspace(0, raw_image.shape[0], 2 * raw_image.shape[0])

    # Perform interpolation on each color channel separately
    interp_func_R = interp2d(np.arange(raw_image.shape[1]), np.arange(raw_image.shape[0]), raw_image[:,:,0], kind='linear')
    interp_func_G = interp2d(np.arange(raw_image.shape[1]), np.arange(raw_image.shape[0]), raw_image[:,:,1], kind='linear')
    interp_func_B = interp2d(np.arange(raw_image.shape[1]), np.arange(raw_image.shape[0]), raw_image[:,:,2], kind='linear')

    # Interpolate each channel
    interpolated_image_R = interp_func_R(new_x, new_y)
    interpolated_image_G = interp_func_G(new_x, new_y)
    interpolated_image_B = interp_func_B(new_x, new_y)

    # Combine the interpolated channels back together
    interpolated_image = np.stack([interpolated_image_R, interpolated_image_G, interpolated_image_B], axis=-1)

    return interpolated_image

interpolated_image = demosaic_bilinear(image)

    # Display or save the interpolated image
plt.imshow(interpolated_image)
    
plt.show()
