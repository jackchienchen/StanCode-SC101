"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics_Extension
from campy.gui.events.mouse import onmouseclicked, onmousemoved


def main():
    graphics = BreakoutGraphics_Extension()
    # Add animation loop here!
    onmouseclicked(graphics.start_function)


if __name__ == '__main__':
    main()
