class MultiFilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        """iterable - исходная последовательность
            funcs - допускающие функции
            judge - решающая функция"""
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):  # возвращает итератор по результирующей последовательности
        output_list = []
        for each_num in self.iterable:
            pos = 0
            neg = 0
            for each_func in self.funcs:
                if each_func(each_num):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                yield each_num


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(MultiFilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
print(list(MultiFilter(a, mul2, mul3, mul5, judge=MultiFilter.judge_all)))
# [0, 30]
