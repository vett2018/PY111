"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        ...  # TODO использовать deque для реализации очереди с приоритетами
        self.pririty_queue = { #словарь дека
            value: deque() for value in range(self.HIGH_PRIORITY, self.LOW_PRIORITY+1)
        }

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        ...  # TODO реализовать метод enqueue
        if priority not in range(self.HIGH_PRIORITY, self.LOW_PRIORITY+1): #точно приоритет тот который существует
            raise ValueError("Не тот приоритет")

        #авнозначная реализация
        # if not isinstance(priority, int) or not self.HIGH_PRIORITY <= priority <= self.LOW_PRIORITY:
        #     raise ValueError("Не тот приоритет")

        self.pririty_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue
        for queue in self.pririty_queue.values():#зять все доступные очереди нашей очереди с приоритетом
            if queue: #если значение не пустое нашей очереди
                    return queue.popleft()

            #можем ли мы извлечь из пустой очереди
        raise IndexError("Очередь Пустая")

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        if not isinstance(ind, int): #проверка на тип данных int
            raise TypeError("Индекс не целый")

        #получить значение длины очереди
        queue = self.pririty_queue[priority]

        #проверка индекса лежит ли он в границах стека между нулем и длиной нашего элемента
        if not 0 <= ind <= len(queue):
        #if not 0 <= ind <= self._stack.__len__(): #аналогично работа с объектами
        #if not 0 <= ind <= self._len
            raise IndexError("Индекс вне границ очереди")

        return queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        #отличается от стека, так как есть словарь со своими
        # очередями поэтому нужно пробежаться по всему словарю и
        # в каждой его реализации очистить словарь
        for queue in self.pririty_queue.values():
            queue.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        #вывести кол-во всех элементов в очереди
        #переопределяем len
        s = 0
        for value in self.pririty_queue.values():
            s += len(value)
        return s


if __name__ == '__main__':
    p = PriorityQueue()
    p.enqueue(1, 0)
    p.enqueue(2, 0)
    p.enqueue(1, 3)
    p.enqueue(4, 0)
    print(p.pririty_queue)
    print(p.dequeue())
    print(p.dequeue())
    print(p.dequeue())
    print(p.dequeue())
