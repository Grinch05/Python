rub = int(input("Введите вашу сумму в рублях"))
valut = input("Введите валюту в которую хотите перевести ваши рубли")
if valut == "доллары":
    v = rub / 91.70
elif valut == "евро":
    v = rub / 98.72
elif valut == "юани":
    v = rub / 12.63
print(f"Ваши {rub} рублей = {v} {valut}")