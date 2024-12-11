import copy

# To test the code run the following command in the terminal or command prompt: python tester.py SantiagoMichael_070L_p2.py
"""
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
"""


def invert(image):
    newim = copyim(image)
    for row in range(0, len(image)):
        for col in range(0, len(image[row])):
            newim[row][col] = 255 - image[row][col]
    # print(newim)
    return newim


"""
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
"""


def blur(image):
    im3 = copyim(image)
    kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
    for row in range(len(im3)):
        for col in range(len(im3[row])):
            if row == 0 or row == len(im3) - 1 or col == 0 or col == len(im3[row]) - 1:
                im3[row][col] = 0
            else:
                weighted_sum = (
                    image[row - 1][col - 1] * kernel[0][0]
                    + image[row - 1][col] * kernel[0][1]
                    + image[row - 1][col + 1] * kernel[0][2]
                    + image[row][col - 1] * kernel[1][0]
                    + image[row][col] * kernel[1][1]
                    + image[row][col + 1] * kernel[1][2]
                    + image[row + 1][col - 1] * kernel[2][0]
                    + image[row + 1][col] * kernel[2][1]
                    + image[row + 1][col + 1] * kernel[2][2]
                )
                total_weights = (
                    kernel[0][0]
                    + kernel[0][1]
                    + kernel[0][2]
                    + kernel[1][0]
                    + kernel[1][1]
                    + kernel[1][2]
                    + kernel[2][0]
                    + kernel[2][1]
                    + kernel[2][2]
                )
                im3[row][col] = weighted_sum // total_weights
    return im3


"""
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
"""


def flip(image):
    newim2 = copyim(image)
    newim2 = newim2[::-1]
    return newim2


"""
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a 2x2 tiled version of the input image. The tile function
    will group pixels in groups of 4 and map each one to one of the 4 tiles
    based on their relative position in the group. That is to say in 
    [[1, 2],
     [3, 4]]
    the number 1 will be in the top left tile, 2 in the top right tile, 
    and so on. Because nearby pixels are similar this will create an image 
    which loops like 4 copies of the same image but slightly different.

    To make the transformation, consider 4 pixels in each iteration 
    of the loop and map them to the corresponding tiles. Each tile will be
    half the length and half the width of the input image.
"""


def tile(image):
    return image


def copyim(image):
    l = []
    for row in image:
        temp = []
        for col in row:
            temp.append(col)
        l.append(temp)
    return l
