import turtle

p = turtle.Pen()
p.pencolor('blue')
p.pensize(5)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)

t = turtle.Turtle()
w = turtle.Screen()
for i in range(5):
    t.forward(100)
    t.right(72)
t = turtle.Turtle()
w = turtle.Screen()
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()