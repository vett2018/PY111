queque = {}
queque [0] = []
queque = {value: [] for value in range(11)}
print(f'пустая очередь в качестве примера \n{queque}')
print("--------------------------------")

def add_to_queque(value, priority, queque):
    queque[priority].append(value)
    return queque

add_to_queque(5, 0, queque) #очередь со значением 5 и наивысшим приоритетом
print(f'добавили \n{queque}')
add_to_queque(-2, 0, queque)
print(f'Добавили в очередь \n{queque}')
print('______________________')


