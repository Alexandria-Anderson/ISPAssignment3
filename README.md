# ISPAssignment3

isp.py converts baby.tiff into a 2D array before preforming Linearization.

File 1.1_WhiteBalancing utilizes the 3 different algorithms for white balancing, and outputs all images alongisde the original image.

File 1.2_ManualWhiteBalancing sets up an interactive environment to select a white patch in the source image, and will automatically white balance the image. All you need to do is run the script, and left click to select the top left and bottom right corners of the white patch. Upon doing so, the window should automatically close and a new window with the original image and the resulting white balanced image should display.

demosaicing.py uses scipy's built-in interp2d to preform bilinear interpolation. 
