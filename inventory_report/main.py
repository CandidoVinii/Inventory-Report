import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def select_file_type(path):
    if path.endswith('.csv'):
        return CsvImporter
    elif path.endswith('.json'):
        return JsonImporter
    elif path.endswith('.xml'):
        return XmlImporter
    else:
        raise ValueError('Invalid format file')


def main():
    pass
    if len(sys.argv) < 3:
        print(ValueError('Verifique os argumentos'), file=sys.stderr)
        return

    *_, path, type = sys.argv

    file_type = select_file_type(path)
    report = InventoryRefactor(file_type).import_data(path, type)
    print(report, end="")


if __name__ == "__main__":
    main()
