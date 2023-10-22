money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

number_months = 0
#после первого месяца
the_rest_of_money = 19000
number_months = 1

while the_rest_of_money <= 0:
    number_months += 1
    the_rest_of_money += salary
    expenses = spend * increase
    the_rest_of_money -= expenses

print("Количество месяцев, которое можно протянуть без долгов:", number_months)
