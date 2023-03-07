from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
     # Сортировка для множества повторяющихся чисел
    # сортировка составляет пустой список о колличестве повторений сохраняется номер и соответсвенно само число
     # TODO реализовать алгоритм сортировки подсчетами
    # найти сначала максимальный
    if not container:
        return  container
    maximum = max(container)
    counts = [0] * (maximum + 1)
    #print(counts)
    for value in container:
        counts[value] = counts[value] + 1
        #print(counts, '\n')
    result = []
    for index, count in enumerate(counts):
        result = result + [index] * count
    #print(result, '\n')
    #print(result)
    return counts, result



mas = [4, 4, 4, 4, 4, 9, 9, 7, 3, 3, 3 ]
print(sort(mas))
