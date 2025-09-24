def ler_arquivo(nome_arquivo):
    """Lê e exibe o conteúdo do arquivo na tela"""
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                print("Arquivo está vazio.")
            else:
                print("Conteúdo do arquivo:")
                print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Ainda não existe nada salvo.")


def escrever_arquivo(nome_arquivo):
    """Escreve um número no arquivo"""
    try:
        numero = float(input("Digite um número: "))
        with open(nome_arquivo, "a") as arquivo:  # "a" = append (adiciona no final)
            arquivo.write(str(numero) + "\n")
        print("Número salvo com sucesso!")
    except ValueError:
        print("Valor inválido. Digite apenas números.")


def calcular_media(nome_arquivo):
    """Calcula e exibe a média dos números no arquivo"""
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            numeros = [float(linha.strip()) for linha in linhas if linha.strip() != ""]
        
        if len(numeros) == 0:
            print("Não há números no arquivo para calcular a média.")
        else:
            media = sum(numeros) / len(numeros)
            print(f"Média dos valores: {media:.2f}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Ainda não existe nada salvo.")
    except ValueError:
        print("Erro: O arquivo contém dados inválidos.")


def main():
    nome_arquivo = "valores.txt"  # pode ser .txt ou .csv

    while True:
        print("\n--- MENU ---")
        print("1 - Ler arquivo")
        print("2 - Escrever número no arquivo")
        print("3 - Mostrar média dos valores")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ler_arquivo(nome_arquivo)
        elif opcao == "2":
            escrever_arquivo(nome_arquivo)
        elif opcao == "3":
            calcular_media(nome_arquivo)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
