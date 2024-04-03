text = input("Введите текст\n").lower()
word = input("Введите слово для поиска: ").lower()
position = text.find(word)

if position != -1:
    print(f"Слово '{word}' найдено на позиции {position}.")
else:
    print(f"Слово '{word}' не найдено в тексте.")
  