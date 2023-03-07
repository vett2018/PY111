from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений
    table = table.copy()

    n = len(table) #длина всего списка списка
    m = len(table[0]) #длина вложенного списка

    for row in range(n-1): #узнаем минимальный по строке
        table[row+1][0] += table[row][0]

    for col in range(m - 1): #узнаем минимальный по столбце
        table[0][col+1] += table[0][col]

    for i in range(1, n): #строки
        for j in range(1, m): #толбцы
            table[i][j] += min(table[i-1][j], table[i][j-1])

    return table


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
