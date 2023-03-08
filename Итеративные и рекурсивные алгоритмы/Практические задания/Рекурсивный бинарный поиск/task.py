from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    # TODO реализовать алгоритм бинарного поиска
    if right_border is None:
        right_border = len(seq)-1

    if left_border > right_border:
        raise ValueError("Нет значения")

    #рассматриваем индексы
    #посчитать центральныйиндекс
    #middle_index = (left_border + right_border)//2
    middle_index = left_border + (right_border - left_border) // 2 # второй способ из за
    # проблем с переполнением значений. Определяем разницу между правой и левой границы что бы определить сколько значений
    middle_value = seq[middle_index] # определили центральное значение
    if value == middle_value:
        while True:
            if not 0 <= middle_index - 1 < len(seq) or seq[middle_index -1] != value: # лежит в границах
                break
            middle_index -= 1
        return middle_index
    elif middle_value > value: #если среднее значение больше нашего искомого
        # значения на необходимо пойти влево нужно сдвинуть границу влево
        right_border = middle_index - 1
    else:
        left_border = middle_index + 1 #левую границу сдвигаем

    return binary_search(value, seq, left_border, right_border)

if __name__ == '__main__':
    #seq = list(range(10))

    seq = list(range(4)) + [3]*6 + list(range(4, 10, 1))
    #binary_search(5.5, seq, 0, 9)
    for value in range(11):
        print(f'value = {value}, idx = {binary_search(value, seq, 0)}')
