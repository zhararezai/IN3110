from http.client import SEE_OTHER
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

import numpy.testing as nt
import numpy as np


def test_color2gray(image, reference_gray):
    
    grayscale_image = numpy_color2gray(image)

    # check that the result has the right shape, type
    assert type(grayscale_image.shape) == tuple
    assert type(image.shape) == type(grayscale_image.shape)
    assert (type(item) == int for item in grayscale_image.shape)

    assert np.array_equal(grayscale_image, reference_gray)
    
    assert grayscale_image[:,:,0].all() == grayscale_image[:,:,1].all()
    assert grayscale_image[:,:,1].all() == grayscale_image[:,:,2].all()


    


def test_color2sepia(image, reference_sepia):
    sepia_image = numpy_color2sepia(image)

   
    assert sepia_image.shape == image.shape #testing the shape
    assert sepia_image.dtype == np.dtype("uint8") #testing the type


    nt.assert_allclose(sepia_image, reference_sepia, atol = 1)

    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    expectedRed = int(sepia_matrix[0][0] *  image[0][4][0] + sepia_matrix[0][1] * image[0][4][1] + sepia_matrix[0][2] * image[0][4][2])
    expectedGreen = int(sepia_matrix[1][0] * image[0][1][0] + sepia_matrix[1][1] * image[0][1][1] + sepia_matrix[1][2] * image[0][1][2])
    expectedBlue = int(sepia_matrix[2][0] * image[0][0][0] + sepia_matrix[2][1] * image[0][0][1] + sepia_matrix[2][2] * image[0][0][2])
    
    assert sepia_image[0][4][0] == expectedRed
    assert sepia_image[0][1][1] == expectedGreen
    assert sepia_image[0][0][2] == expectedBlue

