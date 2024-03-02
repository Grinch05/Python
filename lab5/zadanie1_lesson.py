import turtle
turtle.shape("turtle")
turtle.speed(2)

color = input("введите цвет")
turtle.color(color)
#каркас
turtle.circle(30)
turtle.right(180)
turtle.circle(40)

turtle.penup()
turtle.left(90)
turtle.forward(80)
turtle.pendown()
turtle.right(90)
turtle.circle(50)