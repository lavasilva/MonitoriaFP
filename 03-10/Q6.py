while True:
    codigo_produto = int(input("Digite o código do Produto: "))

    if codigo_produto == 5413:
        break

    valor_produto = float(input("Digite o valor do Produto: "))
    total_estoque = int(input("Total em Estoque do Produto: "))

    if total_estoque <= 2:
        valor_produto = valor_produto * 0.6
        print(f"Produto {codigo_produto} - Desconto de 40%, Novo Valor: {valor_produto}")

    if 3 <= total_estoque <= 5:
        valor_produto = valor_produto * 0.7
        print(f"Produto {codigo_produto} - Desconto de 30%, Novo Valor: {valor_produto}")
    
    if 6 <= total_estoque <= 9:
        valor_produto = valor_produto * 0.8
        print(f"Produto {codigo_produto} - Desconto de 20%, Novo Valor: {valor_produto}")

    if total_estoque >= 10:
        valor_produto = valor_produto * 0.9
        print(f"Produto {codigo_produto} - Desconto de 10%, Novo Valor: {valor_produto}")

