rightCounter = 0
questionsCounter = 0
questions = ["сколько цветов у радуги?", "какой язык мы изучаем?", "Столица России?", "Какой сейчас год?", "Столица Китая?"]
rightAnswers = ["7", "python", "москва", "2024", "пекин"]
while questionsCounter < len(questions):
 answer = input(questions[questionsCounter])
 if answer.lower() == rightAnswers[questionsCounter]:
  print("вы ответили верно")
  rightCounter += 1
  questionsCounter += 1
 else:
  print("вы ответили не верно")
print(f"вы набрали баллов: {rightCounter}")
