from collections import deque


class Queue:
    def __init__(self):
        self.__queue = deque([])

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        return self.__queue.popleft()

    def search(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError

        return self.__queue[index]
