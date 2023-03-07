from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
      # TODO реализуйте сортировку слиянием
    if len(container) == 1:
        return container
    middle = len(container) // 2
    # left = container[:middle] #слайсирование взять индекс от левой части
    # right = container[middle:]
    left = sort(container[:middle]) #слайсирование взять индекс от левой части
    right = sort(container[middle:])
    return _merge(left, right)

def _merge(left_container: list[int], right_container: list[int]) -> list[int]:
    merge_container = [] #складываем элементы
    while True:
        if left_container[0] <= right_container[0]:
            elem = left_container.pop(0)
            merge_container.append(elem)
        else:
            elem = right_container.pop(0)
            merge_container.append(elem)
        if not left_container:
            merge_container = merge_container + right_container
            break
        if not right_container:
            merge_container = merge_container + left_container
            break
        return merge_container

mas = [4, 4, 4, 4, 4, 9, 9, 7, 3, 3, 3 ]
print(sort(mas))
