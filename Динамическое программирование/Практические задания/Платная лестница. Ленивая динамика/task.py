from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать ленивую динамику
    @lru_cache #декоратор для кеша помогает запоминать значения при рекурсии и не только повторное обращение
    #схожий элемент он вычисляет для всех остальных он вытаскивает @lru_cache(maxsize=) maxsize предельный
    # обьем памяти которй можно выставить
    def lazy_dinamic(stairway, n): #на основании n будет рекурсия наша ступенька
        if n == 0 or n == 1: # цена ступеньки
            return stairway[n]
        return stairway[n] + min(lazy_dinamic(stairway, n-1), lazy_dinamic(stairway, n-2))
    return lazy_dinamic(stairway, len(stairway)-1)



if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
