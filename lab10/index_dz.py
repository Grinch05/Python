import random
i = 0
questionsList = ["когда будет хорошая погода?", "сегодня вечером я?", "что со мной случиться?"]
timeList =["Сегодня", "Завтра", "Очень скоро"]
eventList = ["встречу кое кого", "буду радоваться", "найду кошелек"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
while i < 3:
 questions = input("введите свой вопрос")
 if questions in questionsList:
    if i == 0:
        time = timeList[random.randint(0, len(timeList) - 1)]
        print(time)
        i += 1
        continue
    if i == 1:
        event = eventList[random.randint(0, len(eventList) - 1)]
        print(event)
        i += 1
        continue
    if i == 2:
        object = objectList[random.randint(0, len(objectList) - 1)]
        print(object)
        i += 1
 else:
    print("Вопрос плохой")
print("На этом вопросы всё!")
