from collections import deque

class ResultCache:
    def __init__(self, max_size=10):
        self.cache = deque(maxlen=max_size)

    def add_result(self, result):
        self.cache.append(result)

    def get_latest(self):
        return list(self.cache)

    def clear(self):
        self.cache.clear()