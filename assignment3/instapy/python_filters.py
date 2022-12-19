"""pure Python implementation of image filters"""

import numpy as np
from PIL import Image



def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    # iterate through the pixels, and apply the grayscale transform
        
    #the shape/number of pixels of the image
   
    y, x = image.shape[:2]
    gray_image = np.empty_like(image)


    for rad in range(y):
        for kol in range(x):
            red = 0.21 * image[rad][kol][0]
            green = 0.72 * image[rad][kol][1]
            blue = 0.07 * image[rad][kol][2]

            average = (red + green + blue)/3
            
            gray_image[rad][kol][0] = average
            gray_image[rad][kol][1] = average
            gray_image[rad][kol][2] = average

    
    grayscale_img = gray_image.astype("uint8")
    
    gray_image = Image.fromarray(grayscale_img)
    gray_image.save("python_grayscale_image.jpg")
    
    return grayscale_img


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    # Iterate through the pixels
    # applying the sepia matrix


    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]


    y, x = image.shape[:2]
    sepia_image = np.empty_like(image)
    

    for rad in range(y):
        for kol in range(x):
            red = image[rad][kol][0]
            green = image[rad][kol][1]
            blue = image[rad][kol][2]

            
            sepia_image[rad][kol][0] = min(255, (red * sepia_matrix[0][0] + green * sepia_matrix[0][1] + blue * sepia_matrix[0][2]))
            sepia_image[rad][kol][1] = min(255, (red * sepia_matrix[1][0] + green * sepia_matrix[1][1] + blue * sepia_matrix[1][2]))
            sepia_image[rad][kol][2] = min(255, (red * sepia_matrix[2][0] + green * sepia_matrix[2][1] + blue * sepia_matrix[2][2]))

    
    sepiascale_image = sepia_image.astype("uint8")

    sepia_image = Image.fromarray(sepiascale_image)
    sepia_image.save("python_sepiascale_image.jpg")
    
    # don't forget to make sure it's the right type!
    return sepiascale_image

"""im = Image.open("/Users/user/Documents/DigOk/3.år/IN3110/IN3110-zharabr/assignment3/test/rain.jpg")
resized = im.resize((im.width // 2, im.height // 2))
pixels = np.asarray(resized)

python_color2gray(pixels)"""
#python_color2sepia(pixels)
