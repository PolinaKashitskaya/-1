salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
stop = 9

for i in range(stop):
    percent = spend * increase
    spend += percent
    amount_of_money_per_month: int = spend - salary
    money_capital += amount_of_money_per_month

money_capital = round(money_capital) + 1000  # 1000 за первый месяц без процентов

print("Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
