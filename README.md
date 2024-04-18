# ISPAssignment3

isp.py converts baby.tiff into a 2D array before preforming Linearization.

File 1.1_WhiteBalancing utilizes the 3 different algorithms for white balancing, and outputs all images alongisde the original image.

File 1.2_ManualWhiteBalancing sets up an interactive environment to select a white patch in the source image, and will automatically white balance the image. All you need to do is run the script, and left click to select the top left and bottom right corners of the white patch. Upon doing so, the window should automatically close and a new window with the original image and the resulting white balanced image should display.

demosaicing.py uses scipy's built-in interp2d to perform bilinear interpolation. All file paths should be replaced with your local image location. The program relies on the previously white-balanced image to be saved on locally. 

colorcorrection.py performs color space correction, brightness and gamma correction, and file compression. As with demosaicing.py, all file paths should be replaced with your local image location. 

Both demosaicing.py and colorcorrection.py can be run from the terminal or in an IDE like VSCODE.
