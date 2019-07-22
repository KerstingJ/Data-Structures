from queue_list import QueueList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = QueueList()

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.remove_head()

    def len(self):
        return self.storage.length
