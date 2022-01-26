"""
File: bouncing_ball.py
Name: Jack Chen
-------------------------
This algorithm allows a ball to bounce 3 times in the window given.
The ball will be able to free fall from the Starting point(X, Y) given,
thus bounce to the right side until it hits the right side of the window.
This algorithm should include gravity and force reduction from bouncing back into the calculation.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# CONSTANT
VX = 3
VY = 0
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
lives = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    onmouseclicked(ball_movement)
    ball.fill_color = 'black'


def ball_movement(n):
    """
    This function simulates the track of a free fall ball bouncing right.
    This function allows the user to simulates 3 times and no interference during bounce.
    The ball will end up on the starting point every time it hits the window's right side.
    """
    global VX, VY, DELAY, GRAVITY, SIZE, REDUCE, START_X, START_Y, ball, lives
    vertical_move = VY + GRAVITY
    if lives > 0 and ball.x == START_X and ball.y == START_Y:
        # Set to restrict the 3-times bounce limitation and not be interfere by mouse-click during bounce
        while ball.x < window.width-ball.width:  # While not hitting the right side
            if vertical_move >= 0:  # Ball dropping
                ball.move(VX, vertical_move)
                vertical_move += GRAVITY
                if ball.y > window.height-ball.height:  # if hitting the floor, the speed turns negative
                    vertical_move = -vertical_move
                    vertical_move = vertical_move*REDUCE
                pause(DELAY)
            elif vertical_move < 0:  # Ball Bouncing Back
                ball.move(VX, vertical_move)
                vertical_move = vertical_move+GRAVITY
                pause(DELAY)
        window.add(ball, START_X, START_Y)
        lives -= 1
    else:
        pass


if __name__ == "__main__":
    main()
