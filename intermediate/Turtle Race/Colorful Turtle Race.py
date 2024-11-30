from turtle import Turtle, Screen
import random


def start_race(screen):
    is_race_on = False

    # المستخدم يختار اللون
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    # إنشاء السلاحف
    for turtle_index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    # إذا اختار المستخدم لونا، يبدأ السباق
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            # إذا وصلت السلحفاة إلى خط النهاية
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    # سؤال المستخدم إذا كان يريد إعادة السباق
    replay = screen.textinput(title="Play Again?", prompt="Do you want to race again? (yes/no): ")

    # إذا كانت الإجابة بنعم، نعيد السباق
    if replay.lower() == "yes":
        for turtle in all_turtles:
            turtle.goto(x=-230, y=y_positions[all_turtles.index(turtle)])
        start_race(screen)  # إعادة تشغيل السباق


# إعداد نافذة الشاشة
screen = Screen()
screen.setup(width=500, height=400)

# بداية السباق
start_race(screen)

# غلق الشاشة عند النقر
screen.exitonclick()
