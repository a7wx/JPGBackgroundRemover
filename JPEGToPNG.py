# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:26:37 2023

@author: rymas
"""
from PIL import Image
import numpy as np


def convertToPNG(imgArray, pixelToRemove, intensity):
    """Itereates through all values of img_array and detects if a pixel value falls 
    withen the range to turn transparent given intensity and pixelToRemove"""
    newImg = []
    for row in imgArray:
        newRow = []
        for pixel in row:
            # Finds the diferences between the RGB values of each pixel compared to pixelToRemove 
            differences = [abs(pixel[0] - pixelToRemove[0]), abs(pixel[1] - pixelToRemove[1]), abs(pixel[2] - pixelToRemove[2])]
            # Checks differences with intensity, if all three fall within the desired range the pixel is made transparent
            if differences[0] < intensity and  differences[1] < intensity and differences[2] < intensity:
                #Attempt at a slow fade in transparence in edge cases.  Needs Refinement
                alpha = (((sum(differences)/3) / intensity) * 63) // 1
                if alpha < 32:
                    alpha = 0
                newRow.append([pixel[0], pixel[1], pixel[2], alpha])
            else:
                newRow.append([pixel[0], pixel[1], pixel[2], 255])
        newImg.append(newRow)    
    return np.array(newImg).astype(np.uint8)
                

# Load the image using Pillow and a path to a .jpg file
path =  "C:/Users/rymas/OneDrive/Pictures/CatDragon.jpg"
img = Image.open(path)
# img.show()

# Convert the image to a NumPy array
img_array = np.array(img)

# Color that the user wants removed from the image
pixelToRemove = [255,255,255]

# How close a pixel needs to be in color to be removed from an image
intensity = 44

new_img = convertToPNG(img_array, pixelToRemove, intensity)

# Save Image
image = Image.fromarray(new_img, 'RGBA')
# image.show()
savePath = "newImage.png"
image.save(savePath)
