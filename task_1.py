# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv
script_name, *params = argv

PRODUCTIVITY = 0
RATE_PER_HOUR = 1
BONUS = 2

if (not params) or (len(params) != 3):
    print('Параметры вызова: выработка_в_часах, ставка_в_час, премия')
    exit()

productivity = float(params[PRODUCTIVITY])
rate_per_hour = float(params[RATE_PER_HOUR])
bonus = float(params[BONUS])

result = (productivity * rate_per_hour) + bonus
print(f'Заработная плата сотрудника = {round(result,2)}')
