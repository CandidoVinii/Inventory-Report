from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str):
        if "csv" in path:
            return Inventory.open_csv(path, report_type)
        elif "json" in path:
            return Inventory.open_json(path, report_type)
        elif "xml" in path:
            return Inventory.open_xml(path, report_type)
        else:
            raise ValueError("Type not supported")

    @classmethod
    def open_csv(cls, path, report_type):
        with open(path, encoding="utf-8") as file:
            reading = csv.DictReader(file, delimiter=",", quotechar='"')
            if report_type == "simples":
                return SimpleReport.generate(list(reading))
            if report_type == "completo":
                return CompleteReport.generate(list(reading))
            else:
                raise ValueError("Type not supported")

    @classmethod
    def open_json(cls, path, report_type):
        with open(path, "r") as file:
            reading = json.load(file)
        if report_type == "simples":
            return SimpleReport.generate(list(reading))
        if report_type == "completo":
            return CompleteReport.generate(list(reading))
        else:
            raise ValueError("Type not supported")

    @classmethod
    def open_xml(cls, path, report_type):
        with open(path, "r") as file:
            reading = xmltodict.parse(file.read())['dataset']['record']
        if report_type == "simples":
            return SimpleReport.generate(list(reading))
        if report_type == "completo":
            return CompleteReport.generate(list(reading))
        else:
            raise ValueError("Type not supported")
