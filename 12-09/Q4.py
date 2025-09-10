while True:
    nome = input("Digite o nome do atleta (ou 'Sair' para encerrar): ")
    if nome == "Sair":
        break

    saltos = []
    soma = 0  

    for i in range(5): 
        salto = float(input(f"Digite a distância do {i+1}º salto em metros: "))
        saltos.append(salto)
        soma += salto 

    print("\n****Resultado****")
    for i in range(5):
        print(f"{i+1} salto: {saltos[i]} m")

    media = soma / 5
    print(f"Média dos saltos: {media:.2f} m\n")
