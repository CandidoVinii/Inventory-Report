from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 11111
    nome_do_produto = "Caneca de kombi"
    nome_da_empresa = "Fazedora de caneca"
    data_de_fabricação = "2023"
    data_de_validade = "2024"
    numero_de_serie = "1234555"
    intrucoes_de_armazenamento = "Na mão"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricação,
        data_de_validade,
        numero_de_serie,
        intrucoes_de_armazenamento,
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
