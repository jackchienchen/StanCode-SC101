"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
Name: Jack Chen
"""

from campy.gui.events.timer import pause
from breakoutGraphics import BreakoutGraphics


LIVES = 3
FRAME_RATE = 1000 / 120


def main():
    global LIVES
    g = BreakoutGraphics()
    while LIVES > 0 and g.bricks_amount > 0:
        g.ball.move(g.dx, g.dy)
        pause(FRAME_RATE)
        # Dead
        if g.ball.y + g.ball_radius >= g.window.height:
            g.dx = 0
            g.dy = 0
            LIVES -= 1
            g.is_moving = True
            g.reset_game()
        # Left side and Right side
        elif g.ball.x <= 0 or g.ball.x + g.ball_radius >= g.window.width:
            g.dx = -g.dx
        # Top side
        elif g.ball.y <= 0 or g.ball.y + g.ball_radius >= g.window.height:
            g.dy = -g.dy
        # Detect obj
        g.detect_obj()


if __name__ == '__main__':
    main()
