from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set up the game screen
screen = Screen()
screen.bgcolor("black")  # Set the background color of the screen
screen.setup(width=800, height=600)  # Set the dimensions of the screen
screen.title("PONG - The Game")  # Set the title of the screen window
screen.tracer(0)  # Disable automatic screen updates to control when updates happen

# Create paddles, ball, and score objects
r_paddle = Paddle((350, 0))  # Right paddle at initial position (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle at initial position (-350, 0)
ball = Ball()  # Initialize the ball object
score = Score()  # Initialize the score object

# Set up keyboard bindings for paddle movement
screen.listen()  # Tell the screen to listen for key presses
screen.onkey(r_paddle.up, "Up")  # Right paddle moves up when 'Up' arrow key is pressed
screen.onkey(r_paddle.down, "Down")  # Right paddle moves down when 'Down' arrow key is pressed
screen.onkey(l_paddle.up, "w")  # Left paddle moves up when 'W' key is pressed
screen.onkey(l_paddle.down, "s")  # Left paddle moves down when 'S' key is pressed

# Main game loop
game_is_on = True  # Flag to keep the game running
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the ball's movement
    screen.update()  # Manually update the screen to reflect changes
    ball.move()  # Move the ball based on its current speed and direction

    # Detect collision with the top or bottom (ceiling or floor)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Bounce the ball vertically when it hits the top or bottom boundary

    # Detect collision with either paddle (right or left)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:  # Collision with the right paddle
        ball.bounce_x()  # Bounce the ball horizontally
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:  # Collision with the left paddle
        ball.bounce_x()  # Bounce the ball horizontally

    # Detect right paddle miss (ball goes past the right side)
    if ball.xcor() > 380:
        ball.reset()  # Reset the ball to the center
        score.l_point()  # Increment the left player's score (right player missed)

    # Detect left paddle miss (ball goes past the left side)
    if ball.xcor() < -380:
        ball.reset()  # Reset the ball to the center
        score.r_point()  # Increment the right player's score (left player missed)

# Exit the game when the user clicks the screen
screen.exitonclick()
