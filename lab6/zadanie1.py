import turtle
turtle.shape("turtle")
turtle.speed(5)
turtle.color("red")
a = int(input("Введите 5 или 9: "))
if a == 5:
    for i in range(5):
     turtle.forward(150)
     turtle.left(144)
elif a == 9:
    for i in range(9):
     turtle.forward(140)
     turtle.left(160)