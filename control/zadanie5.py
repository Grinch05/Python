import random
i = 0
a = 0
gr = int(input("Введите длину пароля: "))
print(f"Ваш пароль длиною в {gr} символов: ")
while i < gr:
    a = random.randint(0, 10)
    print(a, end = "")
    i += 1