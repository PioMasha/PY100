money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital > 0:
    difference_ = salary - spend
    if difference_ >= 0:
        # всё ок, живем в плюс
        break
    else:
        balance_month = (salary - spend * (1 + increase)) ** month
        money_capital -= balance_month
        month += 1
print(month)
