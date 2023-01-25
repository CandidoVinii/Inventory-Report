from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def mock_product_list():
    return [
        {
            "id": "11111",
            "nome_do_produto": "Caneca de kombi",
            "nome_da_empresa": "Fazedora de caneca",
            "data_de_fabricacao": "2023-01-01",
            "data_de_validade": "2024-01-01",
            "numero_de_serie": "1234555",
            "intrucoes_de_armazenamento": "Na mão",
        }
    ]


def expected_report():
    product_fake = mock_product_list()[0]
    return (
        f"\033[32m{'Data de fabricação mais antiga:'}\033[0m"
        + f" \033[36m{product_fake['data_de_fabricacao']}\033[0m\n"

        f"\033[32m{'Data de validade mais próxima:'}\033[0m"
        + f" \033[36m{product_fake['data_de_validade']}\033[0m\n"

        f"\033[32m{'Empresa com mais produtos:'}\033[0m"
        + f" \033[31m{product_fake['nome_da_empresa']}\033[0m\n"

        "Produtos estocados por empresa:\n"
        F"- {product_fake['nome_da_empresa']}: 1\n"
    )


def test_decorar_relatorio():
    pass  # Seu teste deve ser escrito aqui
    report = ColoredReport(CompleteReport)
    assert report.generate(mock_product_list()) == expected_report()
