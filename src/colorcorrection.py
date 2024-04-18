from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

MXYZ_cam_dcraw = np.array([
    8139,-2171,-663,-8747,16541,2295,-1925,2008,8093
]).reshape(3, 3) / 10000  

MXYZ_cam = MXYZ_cam_dcraw.reshape(3, 3)

MsRGB_XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041]
])

MsRGB_cam = np.dot(MXYZ_cam, MsRGB_XYZ)

MsRGB_cam_normalized = MsRGB_cam / np.sum(MsRGB_cam, axis=1, keepdims=True)

def color_space_correction(image):
    # Reshape the image to a 2D array where each row represents a pixel
    reshaped_image = np.reshape(image, (-1, 3))
    
    # Apply color space correction to all pixels at once
    corrected_pixels = np.dot(reshaped_image, np.linalg.inv(MsRGB_cam_normalized).T)
    
    # Reshape the corrected pixels back to the original image shape
    corrected_image = np.reshape(corrected_pixels, image.shape)
    
    return corrected_image

# Load the image
image_path = "image path"
image = io.imread(image_path)




# Apply color space correction
corrected_image = color_space_correction(image)


# brightness and gamma


def adjust_brightness(image, brightness):
    adjusted_image = np.clip(image + brightness, 0, 255).astype(np.uint8)
    return adjusted_image


def gamma_encoding(image, gamma):
    encoded_image = np.clip(image ** gamma, 0, 255).astype(np.uint8)
    return encoded_image

image = adjust_brightness(corrected_image, 100)
image = gamma_encoding(image, 100)
io.imsave('image path', image)

plt.imshow(image)
plt.show()
