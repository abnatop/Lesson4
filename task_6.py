"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
"""

from itertools import count
from itertools import cycle

iter_from = int(input('Введите начальное значение итератора (целове число): '))
iterator_one = count(iter_from)

for element in iterator_one:
    if element > 1000:
        break
    else:
        print(element)

some_list = ['A', 'B', 'C']
iterator_two = cycle(some_list)

for i in range(100):
    print(f'Элемент {i} = {next(iterator_two)}')
