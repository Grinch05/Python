studentList = ["вася", "петя"]
while True:
    answer = int(input("выберите действие\n"
                       "1-добавить студента\n"
                       "2-удалить студента\n"
                       "3-посмотреть весь список студентов\n"
                       "4-удалить студента по имени\n"
                       "0-выйти из программы\n"))
    if answer not in [1, 2, 3, 4, 0]:
        print("такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("введите имя студента: ").lower()
        
        studentList.append(newStudent)
    elif answer == 2:
        delNumber = int(input("введите номер студента для удаления: "))
        if 0 <= delNumber < len(studentList):
            studentList.pop(delNumber)
        else:
            print("Неверный номер студента")
    elif answer == 3:
        print(studentList)
    elif answer == 4:
        delName = input("введите имя студента для удаления: ").lower()
        if delName in studentList:
            studentList.remove(delName)
        else:
            print("Студент не найден в списке.")
    elif answer == 0:
        break
