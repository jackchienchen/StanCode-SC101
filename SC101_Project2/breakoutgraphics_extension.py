"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Name: Jack Chen
YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

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
FRAME_RATE = 1000 / 120

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics_Extension:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        # Keyword Arguments
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        self.brick_spacing = BRICK_SPACING
        self.brick_width = BRICK_WIDTH
        self.brick_height = BRICK_HEIGHT
        self.brick_offset = BRICK_OFFSET
        self.paddle_offset = PADDLE_OFFSET
        self._dx = 0
        self.ball_dx = self._dx
        self._dy = INITIAL_Y_SPEED
        self.ball_dy = self._dy
        self.ball_radius = BALL_RADIUS
        self.obj = None
        self.lives = 3
        self.bricks_amount = self.brick_rows * self.brick_cols
        self.end_game = GLabel('Game Over')
        self.win_game = GLabel('Game Winner')
        # Window create
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title='Breakout')
        # Paddle create
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'white'
        self.paddle.color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-self.paddle_offset-self.paddle.height)
        # Ball Create
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'white'
        self.ball.color = 'black'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                        y=(self.window.height-self.ball.height)/2)
        # Score Label
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.color = 'black'
        self.window.add(self.score_label, x=0, y=self.score_label.height)
        # Lives Label
        self.lives_count = 3
        self.lives_label = GLabel('Lives Remaining: ' + str(self.lives_count))
        self.window.add(self.lives_label, x=window_width-self.lives_label.width, y=self.lives_label.height)
        # Create Bricks
        self.create_bricks()
        self.brick = GRect(width=self.brick_width, height=self.brick_height)
        # Connect the mouse with paddle
        self.set_ball_velocity()
        self.bricks_detector()
        onmousemoved(self.paddle_control)

    def start_function(self, event):
        if self.lives > 0 and self.bricks_detector is not None:  # Game Continuation Limitation: 1.No lives 2.No Bricks
            if self.ball.x == (self.window.width-self.ball.width)/2 and \
                    self.ball.y == (self.window.height-self.ball.height)/2:  # Mouse Clock only when ball in middle
                while True:  # While loop for ball movement
                    if self.ball.y + self.ball_radius * 2 < self.window.height:  # While ball not touch bottom
                        pause(FRAME_RATE)
                        self.ball.move(self.ball_dx, self.ball_dy)
                        self.ball_detector()  # Method aimed to reflect ball and remove bricks when contact.
                        if self.bricks_amount <= 0:
                            self.game_winner()
                            break
                        self.paddle_reflect()  # Method aimed to reflect ball when ball and paddle are in contact.
                        if self.ball.y <= 0:  # Ball top reflect
                            self.ball_dy = -self.ball_dy
                        if self.ball.x <= 0 or self.ball.x + self.ball_radius * 2 >= self.window.width:
                            # Ball side reflect
                            self.ball_dx = -self.ball_dx
                    else:  # When ball hit bottom: 1. lives-1 2. reset ball
                        self.lives -= 1
                        self.lives_count -= 1
                        self.lives_label.text = 'Lives Remaining: ' + str(self.lives_count)
                        break
                self.ball_reset()
                if self.lives <= 0:
                    self.window.remove(self.ball)
                    self.game_over()

            else:
                pass

    def game_winner(self):
        self.win_game.color = 'black'
        self.win_game.font = '-90'
        self.window.add(self.win_game, x=(self.window.width-self.win_game.width)/2,
                        y=(self.window.height+self.win_game.height)/2)

    def game_over(self):
        self.end_game.color = 'black'
        self.end_game.font = '-90'
        self.window.add(self.end_game, x=(self.window.width-self.end_game.width)/2,
                        y=(self.window.height+self.end_game.height)/2)

    def ball_detector(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball_radius*2, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius*2)
        obj4 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        if obj1 is not None and obj1 is not self.paddle:
            self.window.remove(obj1)
            self.ball_dy = -self.ball_dy
            self.bricks_amount -= 1
            self.score += 10
        elif obj2 is not None and obj2 is not self.paddle:
            self.window.remove(obj2)
            self.bricks_amount -= 1
            self.ball_dy = -self.ball_dy
            self.score += 10
        elif obj3 is not None and obj3 is not self.paddle:
            self.window.remove(obj3)
            self.bricks_amount -= 1
            self.ball_dy = -self.ball_dy
            self.score += 10
        elif obj4 is not None and obj4 is not self.paddle:
            self.window.remove(obj4)
            self.bricks_amount -= 1
            self.ball_dy = -self.ball_dy
            self.score += 10
        self.score_label.text = 'Score: ' + str(self.score)

    def paddle_reflect(self):
        obj1 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        if obj1 is self.paddle:
            self.ball_dy = -self.ball_dy
            for i in range(self.paddle.height//self.ball_dy):
                self.ball.move(self.ball_dx, self.ball_dy)
        elif obj2 is self.paddle:
            self.ball_dy = -self.ball_dy
            for i in range(self.paddle.height//self.ball_dy):
                self.ball.move(self.ball_dx, self.ball_dy)

    def bricks_detector(self):
        for i in range(self.window.width):
            for j in range(self.brick_offset+self.brick.height*self.brick_rows):
                self.obj = self.window.get_object_at(i, j)
                return self.obj

    def ball_reset(self):
        self.set_ball_velocity()
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                        y=(self.window.height-self.ball.height)/2)

    def set_ball_velocity(self):
        self.ball_dx = random.randint(1, MAX_X_SPEED)
        self.ball_dy = random.randint(1, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.ball_dx = -self.ball_dx
        if random.random() > 0.5:
            self.ball_dy = -self.ball_dy

    def paddle_control(self, mouse):
        self.paddle.x = mouse.x-self.paddle.width/2
        self.paddle.y = self.window.height - self.paddle_offset

    def create_bricks(self):
        for i in range(self.brick_rows):
            for k in range(self.brick_cols):
                brick = GRect(width=self.brick_width, height=self.brick_height)
                brick.filled = True
                if (i+1) % 10 == 1 or (i+1) % 10 == 2:
                    brick.fill_color = 'lightcyan'
                elif (i+1) % 10 == 3 or (i+1) % 10 == 4:
                    brick.fill_color = 'aquamarine'
                elif (i+1) % 10 == 5 or (i+1) % 10 == 6:
                    brick.fill_color = 'cyan'
                elif (i+1) % 10 == 7 or (i+1) % 10 == 8:
                    brick.fill_color = 'lightskyblue'
                elif (i+1) % 10 == 0 or (i+1) % 10 == 9:
                    brick.fill_color = 'deepskyblue'
                self.window.add(brick, x=k * (self.brick_width + self.brick_spacing),
                                y=i * (self.brick_height + self.brick_spacing) + self.brick_offset)
