import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Filled Flower Drawing")

# Create turtle
pen = turtle.Turtle()
pen.speed(10)
pen.color("red", "pink")  # Pen color, Fill color

# Function to draw a filled petal
def draw_petal():
    pen.begin_fill()
    pen.circle(50, 60)  # Arc
    pen.left(120)
    pen.circle(50, 60)
    pen.left(120)
    pen.end_fill()

# Draw flower with 6 filled petals
for _ in range(6):
    draw_petal()
    pen.left(60)

# Draw stem with green fill
pen.color("green", "green")
pen.right(90)
pen.penup()
pen.forward(0)
pen.pendown()
pen.begin_fill()
pen.forward(200)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(200)
pen.end_fill()

# Finish
pen.hideturtle()
turtle.done()
