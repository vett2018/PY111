from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени
    if count_stairs < 0:
        raise ValueError("Количество ступеней должно быть не отрицательным числом")

    if count_stairs == 0:
        return [0]
    if count_stairs == 1:
        return [0, 1]

    count_p = [0] * (count_stairs+1) #кол-во путей на еденицу больше так как от нуля список идет
    count_p[0] = 0
    count_p[1] = 1

    for i in range(2, count_stairs + 1):
        count_p[i] = count_p[i-1] + count_p[i-2]
    return count_p



if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(10))  # [0, 1, 1, 2, 3, 5]
