from functools import cache, lru_cache

count = 0

@lru_cache()
def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO реализовать рекурсивный алгоритм
    global count
    count += 1
    if n < 0:
        raise ValueError("Не должно быть отрицательным")

    if n == 0: #o(1)
        return 0
    if n == 1: #o(1)
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2) # o(2^n)

if __name__ == '__main__':
    for i in range(100):
        count = 0
        print(f'i = {i}, res = {fib_recursive(i)}, c = {count},n^2 = {i ** 2}, n^4 = {i ** 4}, 2^n = {2 ** i}')
    # count = 0
    # print(fib_recursive(2))
    # print(count)
    # print(fib_recursive(15))