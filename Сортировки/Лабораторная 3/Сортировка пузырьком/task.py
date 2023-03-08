from typing import Sequence
from operator import lt, gt #lt - больше, gt - меньше
#from .task import sort

def sort(container: Sequence[int], asc: bool = True) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # TODO реализовать алгоритм сортировки пузырьком
    offset = 1
    change = False
    compare = gt if asc else lt
    for len_mas in range(len(container)): #O(N)
        for i in range(0, len(container)-offset): # была O(N), стала O(log(N)
            #if container[i] > container[i+1]:
            if compare(container[i], container[i+1]):
                container[i], container[i+1] = container[i+1], container[i]
                change = True
        if not change: # if change is False
            break
        offset += 1
    return container

_set = [25, 6, 5, 99, 3, 2, 1, 0]
sop = [99, 3, 2, 1, 0, 25, 6, 5]
print(sort(_set, True))
print(sort(sop, False))




