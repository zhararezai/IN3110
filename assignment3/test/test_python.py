from instapy.python_filters import python_color2gray, python_color2sepia
import numpy as np

def test_color2gray(image):
    # run color2gray
    grayscale_image = python_color2gray(image)
    
    # check that the result has the right shape, type
    assert grayscale_image.shape == image.shape
    assert grayscale_image.dtype == np.dtype("uint8")

    # assert uniform r,g,b values
    #dobbel for løkke som sjekker at hver pixel er lik
    x, y = grayscale_image.shape[:2]

    for row in range(x):
        for col in range(y):
            assert grayscale_image[row][col][0] == grayscale_image[row][col][1]
            assert grayscale_image[row][col][1] == grayscale_image[row][col][2]


def test_color2sepia(image):
    # run color2sepia
    # check that the result has the right shape, type
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_image = python_color2sepia(image)

    assert sepia_image.shape == image.shape #testing the shape
    assert sepia_image.dtype == np.dtype("uint8") #testing the type

    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    expectedRed = sepia_matrix[0][0] * image[0][4][0] + sepia_matrix[0][1] * image[0][4][1] + sepia_matrix[0][2] * image[0][4][2]
    expectedGreen = sepia_matrix[1][0] * image[0][1][0] + sepia_matrix[1][1] * image[0][1][1] + sepia_matrix[1][2] * image[0][1][2]
    expectedBlue = sepia_matrix[2][0] * image[0][0][0] + sepia_matrix[2][1] * image[0][0][1] + sepia_matrix[2][2] * image[0][0][2]
    
    assert sepia_image[0][4][0] == int(expectedRed)
    assert sepia_image[0][1][1] == int(expectedGreen)
    assert sepia_image[0][0][2] == int(expectedBlue)




