"""
File: sierpinski.py
Name: Jack Chen
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow


# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	The function will form multiple layers of sierpinski triangle according to the ORDER constant.
	"""

	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: Levels of sierpinski triangles.
	:param length: Length of the first layer of triangle.
	:param upper_left_x: the x coordinate of the first layer of triangle.
	:param upper_left_y: the y coordinate of the first layer of triangle.
	:return: Form multiple layers of sierpinski triangle according to the ORDER constant.
	"""
	if order == 0:  # BASE CASE!
		pass
	else:
		# The top line that forms the triangle.
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# The left line that forms the triangle.
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length*0.5, upper_left_y + length * 0.866)
		# The right line that forms the triangle.
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		window.add(line1)
		window.add(line2)
		window.add(line3)
		# to loop the top left side of the triangle with recursion.
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# to loop the top right side of the triangle with recursion.
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5, upper_left_y)
		# to loop the bottom side of the triangle with recursion.
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.25, upper_left_y + length * 0.866 * 0.5)


if __name__ == '__main__':
	main()