age = int(input("введите возраст"))
if age > 0 and age <= 10:
 print("вы ребёнок")
elif age > 10 and age <= 16:
 print("вы подросток")
elif age > 16 and age <= 25:
 print("вы в расцвете сил")
elif age > 25 and age <= 33:
 print("вы бумер")
elif age > 33 and age < 50:
 print("вы взрослый")
elif age >= 50 and age < 120:
 print("вы пожилой человек")
else:
 print("возраст введён не верно!")