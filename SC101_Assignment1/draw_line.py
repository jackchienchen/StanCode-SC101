"""
File: SECOND draw_line.py
Name: Jack Chen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved


# Constant
SIZE = 20
CLICKS = 0

# global variables
window = GWindow()
circle = GOval(SIZE, SIZE)
x = 0
y = 0
coor = GLabel('')
coor_num = ''


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)
    onmousemoved(follow)


def draw_line(mouse):
    global CLICKS, x, y

    if CLICKS % 2 == 0:  # odd
        CLICKS += 1
        window.add(circle, mouse.x-SIZE//2, mouse.y-SIZE//2)
        x = mouse.x
        y = mouse.y
    else:  # even
        CLICKS += 1
        window.remove(circle)
        window.add(GLine(x, y, mouse.x, mouse.y))


def follow(mouse):
    global coor_num
    coor_num = str(mouse.x) + ', ' + str(mouse.y)
    coor.text = coor_num
    window.add(coor, mouse.x, mouse.y)


if __name__ == "__main__":
    main()
