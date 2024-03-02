counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно") 
#Другие вопросы
answer = input("Аббревиатура нашего предмета?\n")
if answer == "ТРПО" or answer == "трпо":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Вывод результата
print(f"вы набрали баллов {counter}")
