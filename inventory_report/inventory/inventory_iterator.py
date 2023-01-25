from collections.abc import Iterator


class InventoryInterator(Iterator):
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __next__(self):
        product = self._products[self._index]
        if not product:
            raise StopIteration()

        self._products += 1
        return product
