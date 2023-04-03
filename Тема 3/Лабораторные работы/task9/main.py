salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
for month in range(1, months+1):
    if month == 1:
        expenses = spend
    else:
        expenses = prev_spend * (1 + increase)
    prev_spend = expenses
    need_money += expenses - salary

print(int(need_money))



