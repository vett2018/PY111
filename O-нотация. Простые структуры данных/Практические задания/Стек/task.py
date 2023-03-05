from typing import Any


class Stack:
    def __init__(self):
        self._stack = list() #защищенный атрибут, что бы явно неподобраться к элементу
        self._len = 0 #при иницилизации класса общая последовательность равна нулю

    def push(self, elem: Any) -> None:
        # TODO реализовать операцию push
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)
        self._len += 1

        #любой элемент можем добавить в конец
    def pop(self) -> Any: #нет ссылки сколько у нас элементов
        # TODO реализовать операцию pop
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        if not self._stack: #если стек не пустой
            raise IndexError("Стек пустой")
        self._stack.pop()
        self._len -= 1
       # не любой элемент мы можем извлеч с конца

    def peek(self, ind: int = 0) -> Any: #передаем индекс элемента который у нас есть
        # TODO реализовать операцию peek
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int): #проверка на тип данных int
            raise TypeError("Индекс не целый")

        #проверка индекса лежит ли он в границах стека между нулем и длиной нашего элемента
        if not 0 <= ind <= len(self._stack):
        #if not 0 <= ind <= self._stack.__len__(): #аналогично работа с объектами
        #if not 0 <= ind <= self._len
            raise IndexError("Индекс вне границ стека")

        invertirovaniy_index = -1 -ind
        return self._stack(invertirovaniy_index)


    def clear(self) -> None:
        # TODO реализовать операцию clear
        """ Очистка стека. """
        self._stack.clear() #удаление списка (очищаем все объекты которые внутри списка) сам список останется
        self._len = 0
        #self._stack = list() #переопределили сам автоматом удалил
        # for value in self._stack: #второй способ
        #     del value

    def __len__(self) -> int:
        # TODO реализовать операцию __len__
        """ Количество элементов в стеке. """
        print("Зашли в len")
        # returnt len() #базовая хитрость
        return self._len #ПЕРЕОПРЕДЕЛЕНИЕ СВОЕЙ СТРУКТУРЫ
