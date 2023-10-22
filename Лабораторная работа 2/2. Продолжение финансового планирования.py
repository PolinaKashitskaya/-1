salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

stop = 10

for i in range(stop):
    amount_of_money_per_month = ((spend + (spend * increase)) - salary)
    print(amount_of_money_per_month)

money_capital = sum(amount_of_money_per_month) + 1000
#1000 за первый месяц без процентов

print("Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)