import random
botNumber = random.randint(1, 10)
playerNumber = int(input("Введите число: "))
raznica = abs(botNumber - playerNumber)
while playerNumber != botNumber:
    if raznica <= 2:
        print("Горячо!")
    elif raznica <= 4:
        print("Тепло!")
    else:
        print("Холодно!")
    if playerNumber > botNumber:
        print("Ты не угадал, моё число меньше твоего.")
    else:
        print("Ты не угадал, моё число больше твоего.")
    playerNumber = int(input("Введите число: "))
    raznica = abs(botNumber - playerNumber)
print(f"Ты угадал, моё число: {botNumber}")
