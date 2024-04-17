import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.backend_bases import MouseButton

image = imread("data\\baby.jpeg")

fig, ax = plt.subplots(figsize=(10,8))
ax.imshow(image)
ax.set_title("Select a patch in the scene that you expect to be white (Click top left and bottom right corners of patch)")

# Get user input for the coordinates of the patch
print("Click on the top-left and bottom-right corners of the patch.")
coords = plt.ginput(n=2, timeout=0, show_clicks=True,mouse_add=MouseButton.LEFT, mouse_pop = MouseButton.RIGHT, mouse_stop = MouseButton.MIDDLE)
plt.close()
coords = np.array(coords, dtype=int)
#print(coords)

# Extract patch from the image
patch = image[coords[0][1]:coords[1][1], coords[0][0]:coords[1][0]]
r_mean, g_mean, b_mean = np.mean(patch, axis=(0, 1))

#Compute weights
weight_r = 1 /r_mean
weight_g = 1 /g_mean
weight_b = 1/b_mean

#Normalize image
normalized_image = np.zeros_like(image, dtype=np.float64)
normalized_image[:, :, 0] = image[:, :, 0] * weight_r
normalized_image[:, :, 1] = image[:, :, 1] * weight_g
normalized_image[:, :, 2] = image[:, :, 2] * weight_b
normalized_image = np.clip(normalized_image, 0, 1)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image)
axs[0].set_title('Original Image')
axs[1].imshow(normalized_image)
axs[1].set_title('White Balanced Image')
plt.show()





