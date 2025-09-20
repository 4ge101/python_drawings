import turtle

# --- ASCII HEART ---
print("\nASCII Heart:\n")
for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or \
           (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# --- TURTLE HEART ---
print("\nDrawing Turtle Heart...")

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("cyan")
t.pensize(3)
t.speed(5)

t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

turtle.done()