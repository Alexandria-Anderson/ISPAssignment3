import numpy as np
from skimage import io
import matplotlib.pyplot as plt

image = io.imread('data\\baby.jpeg')
image_float = image.astype(np.float64) / 255.0

# White world white balancing
white_world = np.max(image_float, axis=(0, 1))
white_world_balanced = image_float / np.tile(white_world, (image_float.shape[0], image_float.shape[1], 1))

# Gray world white balancing
mean_val = np.mean(image_float, axis=(0, 1))
gray_world_balanced = image_float / np.tile(mean_val, (image_float.shape[0], image_float.shape[1], 1))

# White balancing with preset scales
r_scale, g_scale, b_scale = 1.628906, 1.00000, 1.386719
scaled_balanced = image_float.copy()
scaled_balanced[:, :, 0] *= r_scale
scaled_balanced[:, :, 1] *= g_scale
scaled_balanced[:, :, 2] *= b_scale

scaled_balanced = np.clip(scaled_balanced, 0, 1)
scaled_balanced = (scaled_balanced * 255).astype(np.uint8)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Original image
axes[0, 0].imshow(image)
axes[0, 0].set_title('Original Image')

# White world white balanced image
axes[0, 1].imshow(white_world_balanced)
axes[0, 1].set_title('White World White Balanced')

# Gray world white balanced image
axes[1, 0].imshow(gray_world_balanced)
axes[1, 0].set_title('Gray World White Balanced')

# Scaled white balanced image
axes[1, 1].imshow(scaled_balanced)
axes[1, 1].set_title('Scaled White Balanced')

plt.tight_layout()
plt.show()

