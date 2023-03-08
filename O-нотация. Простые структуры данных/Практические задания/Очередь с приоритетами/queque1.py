def add_to_queque1(value, priority, queque): # без создания всего списка пустых ключей очередь
        #динамическая очередь

    if queque.get(priority):
        queque[priority].append(value)
    else:
        queque[priority] = [value]
    return queque


queue = {}
queue = add_to_queque1(1, 0, queue)
queue = add_to_queque1(24, 40, queue)
queue = add_to_queque1(3, 39, queue)

queue = dict(sorted(queue.items())) #сортировка по ключам словаря
print(queue)