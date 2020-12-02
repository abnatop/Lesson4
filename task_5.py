# Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce() .

from functools import reduce

multiplication = lambda one, two: one * two

even_list = list(range(100, 1001, 2))
result = reduce(multiplication, even_list)

print(result)
