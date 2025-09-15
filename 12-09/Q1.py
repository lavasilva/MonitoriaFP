valores = [3.5, 6.7, 1.0, 4.9]
valores.insert(1, 2.3) # sintaxe = .insert(posicao, valor)
# [3.5, 2.3, 6.7, 1.0, 4.9]
valores.pop()
# [3.5, 2.3, 6.7, 1.0]
valores[2] = 9.2
# [3.5, 2.3, 9.2, 1.0]
extensao_lista = len(valores)
print("Quantidade de elementos:", extensao_lista) # len() length
print("Itens da lista:", valores)
