"""
Завдання 2
Напишіть програму на Python, яка використовує рекурсію для створення фракталу
«сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle

# Constants
SIDES_OF_AN_EQUILATERAL_TRIANGLE = 3
EQUILATERAL_TRIANGLE_INTERNAL_ANGLE = 120

def snowflake_edge(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        size /= 3.0
        snowflake_edge(n - 1, size)
        turtle.left(60)
        snowflake_edge(n - 1, size)
        turtle.right(120)
        snowflake_edge(n - 1, size)
        turtle.left(60)
        snowflake_edge(n - 1, size)

def draw_koch_snowflake(n, size):
    for _ in range(SIDES_OF_AN_EQUILATERAL_TRIANGLE):
        snowflake_edge(n, size)
        turtle.right(EQUILATERAL_TRIANGLE_INTERNAL_ANGLE)
    turtle.done()

# Create The Koch Snowflake
if __name__ == "__main__":
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    draw_koch_snowflake(n=3, size=200)
