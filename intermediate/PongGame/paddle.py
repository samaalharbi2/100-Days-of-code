from turtle import Turtle

# Define the Paddle class which inherits from the Turtle class
class Paddle(Turtle):

    # Initialize the paddle's appearance and position
    def __init__(self, position):
        super().__init__()  # Call the parent class (Turtle) constructor
        self.shape("square")  # Set the paddle shape to a square
        self.color("pink")  # Set the paddle color to pink
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to make it rectangular (tall)
        self.penup()  # Lift the pen so the paddle doesn't leave a trail on the screen
        self.goto(position)  # Set the initial position of the paddle

    # Define the method to move the paddle up
    def up(self):
        new_y = self.ycor() + 20  # Calculate the new Y-coordinate by adding 20 units
        self.goto(self.xcor(), new_y)  # Move the paddle to the new Y-coordinate (same X-coordinate)

    # Define the method to move the paddle down
    def down(self):
        new_y = self.ycor() - 20  # Calculate the new Y-coordinate by subtracting 20 units
        self.goto(self.xcor(), new_y)  # Move the paddle to the new Y-coordinate (same X-coordinate)
