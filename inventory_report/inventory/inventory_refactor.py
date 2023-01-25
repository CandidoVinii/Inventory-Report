from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data += self.importer.import_data(path)
        if type == 'simples':
            return SimpleReport.generate(self.data)
        elif type == 'completo':
            return CompleteReport.generate(self.data)
        else:
            raise ValueError('Type not supported')

    def __iter__(self):
        return InventoryIterator(self.data)