from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data: list):
        data_de_produção = str(date.max)
        validade_mais_proxima = str(date.max)

        empresa_com_mais_produtos = Counter(
            [product["nome_da_empresa"] for product in data]
        ).most_common(1)[0][0]

        for product in data:
            if product["data_de_fabricacao"] < data_de_produção:
                data_de_produção = product["data_de_fabricacao"]

            if product["data_de_validade"] < validade_mais_proxima:
                validade_mais_proxima = product["data_de_validade"]
        return (
            f"Data de fabricação mais antiga: {data_de_produção}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
