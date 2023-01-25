import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def select_type(path):
    if path.endswith('.csv'):
        return CsvImporter

    if path.endswith('.json'):
        return JsonImporter

    if path.endswith('.xml'):
        return XmlImporter


def main():
    pass
    if len(sys.argv) < 3:
        return sys.stderr.write('Verifique os argumentos\n')

    path = sys.argv[1]
    type = sys.argv[2]

    file = select_type(path)
    report = InventoryRefactor(file).import_data(path, type)

    print(report, end="")
