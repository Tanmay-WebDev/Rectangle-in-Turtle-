import turtle

turtle.Screen().bgcolor("#6bb2ed")

screenSize = turtle.Screen()
screenSize.setup(500 , 700)

turtle.title("Welcome To Turtle - Rectangle")

board = turtle.Turtle()

for i in range(2):
    board.forward(200)
    board.left(90)
    board.forward(100)
    board.left(90)

turtle.done()
