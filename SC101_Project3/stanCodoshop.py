"""
File: stanCodoshop.py
Name: Jack Chen
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return math.sqrt((red-pixel[0])**2+(green-pixel[1])**2+(blue-pixel[2])**2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    avg_pixel = []
    for pixel in pixels:
        if len(avg_pixel) == 0:
            avg_pixel.append(pixel.red)
            avg_pixel.append(pixel.green)
            avg_pixel.append(pixel.blue)
        else:
            avg_pixel[0] += pixel.red
            avg_pixel[1] += pixel.green
            avg_pixel[2] += pixel.blue

    return list(map(lambda num: num//len(pixels), avg_pixel))


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    pixel_avg = get_average(pixels)  # [r, g, b]
    min_dis = 0
    best_pixel = None
    for pixel in pixels:
        if pixel is pixels[0]:
            min_dis = get_pixel_dist(pixel_avg, pixel.red, pixel.green, pixel.blue)
            best_pixel = pixel
        else:
            if min_dis > get_pixel_dist(pixel_avg, pixel.red, pixel.green, pixel.blue):
                best_pixel = pixel
                min_dis = get_pixel_dist(pixel_avg, pixel.red, pixel.green, pixel.blue)
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
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            lst = []
            result_pixel = result.get_pixel(x, y)
            for img in images:
                lst.append(img.get_pixel(x, y))
            result_pixel.red = get_best_pixel(lst).red
            result_pixel.green = get_best_pixel(lst).green
            result_pixel.blue = get_best_pixel(lst).blue
    # ----- YOUR CODE ENDS HERE ----- #
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
