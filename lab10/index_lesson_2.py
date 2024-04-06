import random
timeList =["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
znakList = ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]
while True:
 znak = input("введите знак Зодиака")
 if znak in znakList:
  time = timeList[random.randint(0, len(timeList) - 1)]
  event = eventList[random.randint(0, len(eventList) - 1)]
  object = objectList[random.randint(0, len(objectList) - 1)]
  print(time + " " + event + " " + object)
  next = input("хотите попробовать ещё раз?")
 else:
  print("вы ввели некоректынй знак зодиака")
  continue
 if next.lower() == "да" or next.lower() == "yes": 
  continue 
 else:
  print("Приходите ещё за новыми предсказаниями!")
  break