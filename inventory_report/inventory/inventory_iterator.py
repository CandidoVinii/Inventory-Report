from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list):
        self._list = list
        self._index = 0

    def __next__(self):
        try:
            item = self._list[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return item
