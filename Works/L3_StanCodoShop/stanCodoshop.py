"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------

This algorithm will be able to choose the best pixels out of the images provided.
In other words, the algorithm will be able to remove the human figures from the images,
forming a scenery without human.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    return ((red - pixel.red)**2 + (blue - pixel.blue)**2 + (green - pixel.green)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    sum_red = 0
    sum_blue = 0
    sum_green = 0
    for i in range(len(pixels)):
        sum_red += pixels[i].red
        sum_green += pixels[i].green
        sum_blue += pixels[i].blue
    return [sum_red//len(pixels), sum_green//len(pixels), sum_blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    best_pixel_dist = ((pixels[0].red - avg[0]) ** 2 + (pixels[0].green - avg[1]) ** 2 +
            (pixels[0].blue - avg[2]) ** 2) ** 0.5
    best_pixel = pixels[0]
    i = 1
    for i in range(len(pixels)):
        next_pixel_dist = ((pixels[i].red - avg[0]) ** 2 + (pixels[i].green - avg[1]) ** 2 +
            (pixels[i].blue - avg[2]) ** 2) ** 0.5
        if next_pixel_dist < best_pixel_dist:
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    '''
    green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    print(get_average([red_pixel, green_pixel, green_pixel, blue_pixel]))
    '''
    for x in range(width):  # To get all the pixels in the images with for loop: x for width y for heigth
        for y in range(height):
            photos = []  # setting a list for images' pixel
            for a in range(len(images)):  # to form a list of pixels for each (x, y)
                photos.append(images[a].get_pixel(x, y))
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = get_best_pixel(photos).red  # get each (r,g,b) for each result's (x, y)
            result_pixel.green = get_best_pixel(photos).green
            result_pixel.blue = get_best_pixel(photos).blue
        ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
