import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Black Face Drawing")

# Create turtle
pen = turtle.Turtle()
pen.speed(10)

# Draw the black face (circle)
pen.penup()
pen.goto(0, -100)  # Move to start position
pen.pendown()
pen.color("black", "black")  # Outline black, fill black
pen.begin_fill()
pen.circle(100)  # Face radius
pen.end_fill()

# Draw eyes (white circles)
pen.penup()
pen.goto(-40, 40)
pen.pendown()
pen.color("white", "white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

pen.penup()
pen.goto(40, 40)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Draw smile (black arc)
pen.penup()
pen.goto(-50, -20)
pen.pendown()
pen.color("white")  # Smile color
pen.width(5)
pen.setheading(-60)
pen.circle(50, 120)  # Arc for smile

# Finish
pen.hideturtle()
turtle.done()
