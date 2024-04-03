studentList = ["вася", "петя"]
studentPoint = [1, 2]
while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента и оценку\n"
                       "2-удалить студента\n"
                       "3-посмотреть весь список студентов\n"
                       "4-удалить студента по имени\n"
                       "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента: ").lower() 
        newPoint =  int(input("введите оценку студента (от 1 до 5): "))
        if 1 <= newPoint <= 5:
            studentList.append(newStudent)
            studentPoint.append(newPoint)
        else:
         print("Оценка должна быть в диапазоне от 1 до 5.")
    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления: "))
        if 0 <= delNumber < len(studentList):
            studentList.pop(delNumber)
            studentPoint.pop(delNumber)
    elif answer == 3:
        i=0
        while i < len(studentList):
         print(studentList[i], "-", studentPoint[i])
         i += 1
    elif answer == 4:
        delName = input("введите имя студента для удаления: ").lower()
        if delName in studentList:
            index = studentList.index(delName)
            studentList.remove(delName)
            studentPoint.pop(index)
            print("Студент удалён из списка.")
        else:
            print("Студент не найден в списке.")
    elif answer == 0:
        break
