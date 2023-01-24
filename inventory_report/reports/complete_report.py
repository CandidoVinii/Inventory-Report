from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(data: list):
        simple_Report = SimpleReport.generate(data)
        products_industry = {}

        for product in data:
            if product["nome_da_empresa"] in products_industry:
                products_industry[product["nome_da_empresa"]] += 1
            else:
                products_industry[product["nome_da_empresa"]] = 1

        companies = ""
        for company, quantity in products_industry.items():
            companies += f"- {company}: {quantity}\n"

        return (
            f"{simple_Report}\n"
            f"Produtos estocados por empresa:\n{companies}"
        )
