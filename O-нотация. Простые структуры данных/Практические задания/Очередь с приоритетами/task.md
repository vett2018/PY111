Очередь с приоритетами — это разновидность очереди, где каждый элемент имеет свой приоритет.  
Элементы с высшим приоритетом обрабатываются раньше элементов с низшим приоритетом.  
Операции с очередью с приоритетами похожи на операции с обычной очередью, но вместо простой очереди выполнения по порядку, она может выполняться в соответствии с приоритетом элементов.

- `enqueue` (добавление элемента в очередь) - добавляет элемент в очередь с учетом его приоритета.
- `dequeue` (удаление элемента из очереди) - удаляет элемент с начала очереди.
- `peek` (просмотр элемента в начале очереди) - возвращает элемент в начале очереди без его удаления.
- `clear` - очистка очереди. 
- `__len__` - получение текущего количества элементов в очереди.
