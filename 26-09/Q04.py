def cadastrar_nomes():
    arquivo = open("nomes.txt", "w")

    for i in range(6):
        nome = input(f"Digite o nome e sobrenome da pessoa {i+1}: ")
        arquivo.write(nome + "\n")

    arquivo.close()


def editar_nomes():
    arquivo = open("nomes.txt", "r")
    nomes = arquivo.read().splitlines()  
    arquivo.close()

    for i in range(len(nomes)):
        atual = nomes[i] 
        print(f"\nNome atual: {atual}")
        resposta = input("Deseja alterar este nome? (s/n): ").strip().lower()

        if resposta == "s":
            novo_nome = input("Digite o novo nome e sobrenome: ")
            nomes[i] = novo_nome

        arquivo = open("nomes.txt", "w")
        for nome in nomes:
            arquivo.write(nome + "\n")  
        arquivo.close()


# nosso programa principal!!!

def main():
    cadastrar_nomes()
    editar_nomes()

    print("\nConteúdo final do arquivo:")
    arquivo = open("nomes.txt", "r")
    print(arquivo.read())
    arquivo.close()

main()