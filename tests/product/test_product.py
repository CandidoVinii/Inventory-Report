from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, "Caneca", "Fallen", "18-01-2023", "18-01-2023", "1800", "armário"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Caneca"
    assert product.nome_da_empresa == "Fallen"
    assert product.data_de_fabricacao == "18-01-2023"
    assert product.data_de_validade == "18-01-2023"
    assert product.numero_de_serie == "1800"
    assert product.instrucoes_de_armazenamento == "armário"
