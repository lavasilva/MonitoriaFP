#Desenvolva  um  programa  que  escreva  em  um  arquivo  de  texto  (.txt  ou  .csv)  10 
#palavras-chave (o usuário que deve informar as palavras por input), onde cada palavra 
#deve ser registrada em uma linha do arquivo. 
#Em  seguida,  desenvolva  uma  função  que  recebe  uma  determinada  palavra  e 
#verifique se essa palavra está contida no arquivo de texto de palavras-chave (para isso 
#deve ser realizada a leitura do arquivo).  
#-  Retorne True para o caso da palavra existir no arquivo e retorne False 
#para o caso da palavra não existir no arquivo. 
#No programa principal, após a criação do arquivo com as palavras-chave, realize a 
#chamada da função criada e imprima o valor retornado.

def palavra_existe(palavra, nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        palavras = [linha.strip() for linha in linhas]

        return palavra in palavras


def main():
    nome_arquivo = "palavras.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        print("Digite 10 palavras-chave:")

        for i in range(10):
            palavra = input(f"Palavra {i+1}: ")
            arquivo.write(palavra + "\n") 

    palavra_busca = input("Digite uma palavra para verificar se está no arquivo: ")

    resultado = palavra_existe(palavra_busca, nome_arquivo)

    print("Resultado da busca:", resultado)

main()
