import turtle
i = 0
size = int(input("Введите  радиус первого круга: "))
colorList = [ "blue","orange","green","red"]
turtle.shape("turtle")
turtle.speed(10)


while i < 4:
 turtle.color(colorList[i])
 turtle.penup()
 turtle.right(90)
 turtle.forward(size/3)
 turtle.left(90)
 turtle.pendown()
 turtle.circle(size)
 size = size+size/2
 i += 1
