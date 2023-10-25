money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

#после первого месяца
the_rest_of_money = 19000
number_months = 1

while True:
    number_months += 1
    the_rest_of_money += salary
    percent = spend * increase
    spend += percent
    the_rest_of_money -= spend
    if the_rest_of_money < 0:
        number_months -= 1
        break

print("Количество месяцев, которое можно протянуть без долгов:", number_months)
