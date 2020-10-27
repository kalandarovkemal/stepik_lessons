from functools import partial
import operator as op

# В следующем примере показано, что у функции int есть аргументы первый - это строка " ", содержание которой
# нужно перевести в целое число, а второй аргумент - это тип исчисления, то есть двоичная система, десятичная и т.д.
x = int('1101', base=2)
print(x)
# Выводом будет число 13 так как в двоичной 1101 --> 13 в десятичной

#  Если мы хотим, переиспользовать все что делает функция но поменять определенный аргумент, на тот который нам нужен,
# то для этого используем метод partial как показано на следующем примере

int_2 = partial(int, base=2)
a = int_2('1101')
print(a)
b = int_2('1110')
print(b)

'''Так как мы воспользовались методом partial из библиотеки functools, и передали в переменную int_2 функцию int
со вторым аргументом base=2, то теперь при каждом вызове переменной int_2('') Переданное ей число в двоичной системе 
будет выводиться в десятичной системе, при этом каждый раз явно указывать второй аргумент - не надо '''

a = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskel', 'Curry'),
    ('John', 'Backus')
]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(a)
sort_by_last(a)
print(a)

b = ['abc', 'bca', 'abb']
sort_by_last(b)
print(b)
