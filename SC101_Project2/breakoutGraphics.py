"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman,and Jerry Liao
Name: Jack Chen (2022 Re-write version)
This program display a game of Brick Breaker.
Lives: 3
End Game Criteria: 1. Destroy all Bricks 2. No life left
"""
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

# Constants not allowing to change
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # 變數放於此而不是直接使用CONSTANT，因為若coder端使用attribute改變數值，下方methods不會跟著改，若使用CONSTANT會無法調整。
    def __init__(self, brick_spacing=BRICK_SPACING, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET,
                 ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_heigth=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, title='Breakout_Game'):
        # Variables Used
        self.paddle_offset = PADDLE_OFFSET
        self.brick_offset = brick_offset
        self.brick_row = BRICK_ROWS
        self.brick_col = BRICK_COLS
        self.brick_height = BRICK_HEIGHT
        self.brick_width = BRICK_WIDTH
        self.brick_spacing = BRICK_SPACING
        self.game_start = True
        self.ball_radius = BALL_RADIUS
        self.bricks_amount = BRICK_COLS*BRICK_ROWS

        # Create Window
        window_width = brick_width*brick_cols+(brick_cols-1)*brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(window_width, window_height)

        # Create Paddle  # The hard part is to limit the paddle in the window.
        self.paddle = GRect(paddle_width, paddle_heigth, x=(window_width - paddle_width) // 2,
                            y=window_height - paddle_offset - paddle_heigth)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)

        # Create Ball
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width//2 - ball_radius, y=window_height//2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'white'
        self.ball.color = 'black'
        self.window.add(self.ball)

        # Mouse Functions
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_game)

        # Build Bricks
        self.build_bricks()

        # Ball Move
        self.dx = 0
        self.dy = 0
        self.is_moving = True

    def detect_obj(self):
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                detect = self.window.get_object_at(x, y)
                if detect:
                    if detect is self.paddle:
                        if self.dy > 0:  # How this works? Cause it will be stuck in the paddle?
                            self.dy = -self.dy  # 若下方elif也設立 self.dy < 0 會造成卡在paddle上方
                    elif detect is not self.paddle:
                        self.window.remove(detect)
                        self.bricks_amount -= 1
                        self.dy = -self.dy
                    return

    def start_game(self, _):
        if self.is_moving:
            self.dx = random.randrange(1, MAX_X_SPEED)
            self.dy = INITIAL_Y_SPEED
            self.is_moving = False

    def reset_game(self):  # Repositioning the ball
        self.window.add(self.ball, x=self.window.width//2 - self.ball_radius, y=self.window.height//2-self.ball_radius)

    def move_paddle(self, mouse):  # To limit the paddle to fit in the window.
        #  需要設立這兩個elif 來判定邊界
        if self.paddle.width//2 < mouse.x < self.window.width - self.paddle.width//2:  # 中間合理區
            self.window.add(self.paddle, mouse.x-self.paddle.width//2, self.window.height -
                            self.paddle_offset - self.paddle.height)
        elif mouse.x < self.paddle.width//2:  # 左邊過邊界
            self.window.add(self.paddle, 0, self.window.height - self.paddle_offset - self.paddle.height)
        elif mouse.x > self.window.width - self.paddle.width//2:  # 右邊過邊界
            self.window.add(self.paddle, self.window.width-self.paddle.width, self.window.height -
                            self.paddle_offset - self.paddle.height)

    def build_bricks(self):
        for y in range(self.brick_offset, self.brick_offset+self.brick_row*(self.brick_height+ self.brick_spacing),
                       self.brick_height+self.brick_spacing):
            # (brick's y starting point, last brick's next y,b2b spacing)
            for x in range(0, self.window.width, self.brick_spacing+self.brick_width):
                bricks = GRect(self.brick_width, self.brick_height)
                bricks.filled = True
                bricks.color = 'black'
                bricks.fill_color = 'black'
                self.window.add(bricks, x, y)

