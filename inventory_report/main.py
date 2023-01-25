import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    pass
    importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}

    if len(sys.argv) == 3:
        file_type = sys.argv[1].split(".", 1)[1]
        relatory = InventoryRefactor(importers[file_type]).import_data(
            sys.argv[1], sys.argv[2]
        )

        sys.stdout.write(relatory)
        return relatory
    else:
        sys.stderr.write("Verifique os argumentos\n")


if __name__ == "__main__":
    main()
