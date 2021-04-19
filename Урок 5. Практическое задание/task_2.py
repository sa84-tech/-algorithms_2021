"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""
from collections import defaultdict


def add_hex_nums(_hex_num):
    hex_sum = hex(int(''.join(_hex_num[0]), 16) + int(''.join(_hex_num[1]), 16))
    return list(str(hex_sum)[2:].upper())


def mul_hex_nums(_hex_num):
    hex_mul = hex(int(''.join(_hex_num[0]), 16) * int(''.join(_hex_num[1]), 16))
    return list(str(hex_mul)[2:].upper())


hex_nums = defaultdict(list)

# ввод строки с числами через пробел
hex_str = 'A2 C4F'

for i, num in enumerate(hex_str.split(' ')):
    hex_nums[i] = list(num)

print(f'{hex_nums[0]} + {hex_nums[1]} =', add_hex_nums(hex_nums))
print(f'{hex_nums[0]} * {hex_nums[1]} =', mul_hex_nums(hex_nums))
