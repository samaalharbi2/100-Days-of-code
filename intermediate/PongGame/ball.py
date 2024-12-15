from turtle import Turtle

# Define the Ball class, which inherits from the Turtle class
class Ball(Turtle):

    def __init__(self):
        # Initialize the Ball object using the Turtle class constructor
        super().__init__()
        self.shape("square")  # Set the shape of the ball to a square
        self.color("blue")  # Set the color of the ball to blue
        self.penup()  # Lift the pen so it doesn't draw on the screen
        self.x_move = 10  # Set the ball's horizontal movement speed (initially 10 units per frame)
        self.y_move = 10  # Set the ball's vertical movement speed (initially 10 units per frame)
        self.move_speed = .1  # Set the initial move speed (lower value = faster)

    def move(self):
        # Move the ball by updating its position based on x_move and y_move
        new_x = self.xcor() + self.x_move  # Get the current x position and add the x_move
        new_y = self.ycor() + self.y_move  # Get the current y position and add the y_move
        self.goto(new_x, new_y)  # Move the ball to the new position (new_x, new_y)

    def bounce_y(self):
        # Invert the vertical direction of the ball (bounce on the top/bottom walls)
        self.y_move *= -1  # Reverse the direction of movement along the y-axis
        self.move_speed *= 0.9  # Increase the ball's speed slightly by decreasing move_speed

    def bounce_x(self):
        # Invert the horizontal direction of the ball (bounce on the paddles)
        self.x_move *= -1  # Reverse the direction of movement along the x-axis
        self.move_speed *= 0.9  # Increase the ball's speed slightly by decreasing move_speed

    def reset(self):
        # Reset the ball to the center of the screen
        self.goto(0, 0)  # Move the ball to the center of the screen (coordinates 0, 0)
        self.move_speed = .1  # Reset the ball's speed to its initial value
        self.bounce_x()  # Make the ball bounce in the x direction (change direction after reset)
