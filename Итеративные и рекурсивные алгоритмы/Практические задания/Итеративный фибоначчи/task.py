def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO написать итеративный алгоритм чисел Фибоначчи
    if n < 0:
        raise ValueError("Не должно быть отрицательным")
    a = 0
    b = 1
    if n == 0: #o(1)
        return a
    if n == 1: #o(1)
        return b

    for _ in range(2, n+1): #o(N)
        a, b = b, a + b # a = b # b = a + b

    return b #сумма предыдуших элементов

if __name__ == '__main__':
    print(fib_iterative(2))
    print(fib_iterative(54))