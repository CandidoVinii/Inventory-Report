from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.csv_importer import CsvImporter


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def __save_data(self, path: str) -> None:
        imported_data = self.importer.import_data(path)
        for data_product in imported_data:
            self.data.append(data_product)

    def import_data(self, path: str, rel_type: str) -> str:
        self.__save_data(path)

        if rel_type.lower() == "simples":
            relatory = SimpleReport.generate(self.data)
        elif rel_type.lower() == "completo":
            relatory = CompleteReport.generate(self.data)

        return relatory


if __name__ == "__main__":
    instance = InventoryRefactor(CsvImporter)
    instance.import_data(
        "inventory_report/data/inventory.csv", "simples"
    )
    iterator = iter(instance)
    first = next(iterator)
    second = next(iterator)
    print(f"Primeiro elemento: {first}")
    print(f"Segundo elemento: {second}")
