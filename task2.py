import turtle


def koch_curve(t, level, size):
    if level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, level, size):
    for _ in range(3):
        koch_curve(t, level, size)
        t.right(120)


def draw_koch_snowflake(level, size=700):

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / level)
    t.pendown()

    koch_snowflake(t, level, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Enter the recursion level for the Koch snowflake: "))
        draw_koch_snowflake(level)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")