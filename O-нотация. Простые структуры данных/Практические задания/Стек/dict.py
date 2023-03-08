class My:
    def __init__(self):
        self.data = dict()

    def add(self, key, value: list):
        if self.data.get(key):# проверка по ключу если есть ключ то мы его расширяем
            # если нет то заново записываем
            self.data[key].extend(value)
        else:
            self.data[key] = value

    def __str__(self): #через print str
        return f"{self.__dict__['data']}"

    def __repr__(self):
        return f"{self.__dict__['data']}"

    def __len__(self): #возвращаем не просто значение ключей, а возвращаем кол-во наших значений
        s = 0
        for key, value in self.data.items():
            s += len(value)
        return s

if __name__ == '__main__':
    a = My()
    a.add(1, [1, 2, 2])
    a.add(1, [1, 2, 3])
    a.add(2, [1, 2, 3])
    print(a)
    #print(len(a)) #не может вызвать так как сложная структура надо определять len но можно вызвать len(a.data)
    print(len(a.data))
    print(len(a))