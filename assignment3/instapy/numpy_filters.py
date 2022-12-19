"""numpy implementation of image filters"""

from typing import Optional
import numpy as np
from PIL import Image


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    # Hint: use numpy slicing in order to have fast vectorized code
    ...
    # Return image (make sure it's the right type!)
    gray_image = np.empty_like(image)
    
    #print("hei numpy_filters grayfilter")

    red = image[:,:,0] * 0.21
    green = image[:,:,1] * 0.72
    blue = image[:,:,2] * 0.07
    
    average = (red + green + blue)/3

    gray_image[:,:,0] = average
    gray_image[:,:,1] = average
    gray_image[:,:,2] = average

    grayscale_img = gray_image.astype("uint8")

    gray_image = Image.fromarray(grayscale_img)
    gray_image.save("numpy_grayscale_image.jpg")
    
    return grayscale_img


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    
    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    
    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    
    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image = np.empty_like(image)

    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ] * k

    sepia_image = np.einsum('ijk,lk -> ijl', image, sepia_matrix)

    sepia_image = sepia_image.clip(max=255)


    sepiascale_image = sepia_image.astype("uint8") 

    sepia_image = Image.fromarray(sepiascale_image)
    sepia_image.save("numpy_sepiascale_image.jpg")
   
    # Return image (make sure it's the right type!)
    return sepiascale_image


im = Image.open("/Users/user/Documents/DigOk/3.år/IN3110/IN3110-zharabr/assignment3/test/rain.jpg")
resized = im.resize((im.width // 2, im.height // 2))
pixels = np.asarray(resized)

numpy_color2gray(pixels)