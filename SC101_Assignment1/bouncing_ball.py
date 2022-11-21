"""
File: SECOND Bouncing ball
Name: Jack Chen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
LIVES = 3

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.filled = 'black'
    window.add(ball)
    onmouseclicked(ball_drop)  # 每次Click我就執行一次


def ball_drop(_):
    global LIVES
    vy = 0
    if ball.x == START_X and ball.y == START_Y:
        while LIVES > 0:
            if ball.y+SIZE >= window.height:
                vy *= -REDUCE
            if ball.x+SIZE >= window.width:  # 出現bug!!!!
                LIVES -= 1  # 還是lives被扣光？
                window.remove(ball)  # 若remove ball, 會導致下面的ball.move()執行, 導致
                break
            ball.move(VX, vy)  # Tricky, 如果將.move擺放while loop下方．會導致第二次彈跳正負值反覆
            vy += GRAVITY
            pause(DELAY)
        window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
