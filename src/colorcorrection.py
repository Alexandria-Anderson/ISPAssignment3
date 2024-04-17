from skimage import io
import numpy as np
import matplotlib.pyplot as plt

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
    reshaped_image = np.reshape(image, (-1, 3))
    corrected_pixels = np.dot(reshaped_image, np.linalg.inv(MsRGB_cam_normalized).T)
    corrected_image = np.reshape(corrected_pixels, image.shape)
    
    return corrected_image

image_path = "data/baby.jpeg"
image = io.imread(image_path)

corrected_image = color_space_correction(image)

plt.imshow(corrected_image)
plt.show()
