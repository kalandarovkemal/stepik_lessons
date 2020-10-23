# r (read) - Открыть для чтения (по умолчанию стоит этот режим, если не указывать явно)
# w (write) - Открыть для записи, содержимое файли стирается
# a (append) - Открыть для записи, запись введется в конец
# b (binary) - Открывает файл в бинарном режиме
# t (text) - Открыть в текстовом режиме (по умолчанию стоит тесктовый режим) - нужен если файл записан в бинарном режиме
# r+ - Открыть и для чтения и для записи
# w+ - Открыть и для чтения и для записи, в отличае от предыдущего режиме, этот стирает все предыдущие записи
# P.S. Все вышеперечисленные режимо можно исползоватьт в совместном режиме, Наример: rb
f = open('sample.txt', 'r')

# Если мы знаем сколько конкреино сиprint(reversed_lst)мволов надо считать, то можем передать колчисетво в функцию read(n)

# a = f.read(5)

# print(a)
# First

# Так как мы считали в предыдущем примере первые пять символов, то следующий пример считает все остальное, после преды-
# дущего считывания

# b = f.read()


# print(b)
#  line
# Second line
# Third line

# Метод splitlines поменяет содержимое на список из содержимого файла, каждая новая строка при этом будет считываться,
# как новый элемент :  ['First line', 'Second line', 'Third line']

# b = b.splitlines()


# Следующая функция выведет все содержимое файла у учетом "скрытых" символов: \n, \t....
# print(repr(b))

#  'First line\nSecond line\nThird line\n'

# Для того что бы считывать содержимое файла без дополнительных пробельних символов используем метод strip

# c = f.readline().rstrip()
# print(repr(c))
#
# 'First line'

# Для того что бы считать все содержимое в качестве строки, чаще всего используют цикл for

for line in f:
    line = line.rstrip()
    print(repr(line))

#  Вывод будет следующим:
# 'First line'
# 'Second line'
# 'Third line'

# Если мы пользуемся функцией open(), то обязательно должны, после всех необходимых операций вызвать функцию close()

f.close()
