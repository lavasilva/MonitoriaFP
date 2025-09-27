def registrar_votos():
    arquivo = open("votos.txt", "w") # comando 'w' abre arq e escreve

    print("Votação entre os filmes:\n1 - Star Wars\n2 - Star Trek")
    for i in range(10):
        voto = input(f"Pessoa {i+1}, digite seu voto (1 ou 2): ")
        arquivo.write(voto + "\n")

    arquivo.close()


def apurar_votos():
    arquivo = open("votos.txt", "r")
    votos = arquivo.read().splitlines()  
    arquivo.close()

    # splitlines() lê o arquivo sem contar com \n's

    star_wars = votos.count("1") 
    star_trek = votos.count("2")

    # "count()" conta o número de vezes que um elemento específico aparece em uma sequência

    if star_wars > star_trek:
        vencedor = "Star Wars"
        qtde = star_wars
    elif star_trek > star_wars:
        vencedor = "Star Trek"
        qtde = star_trek
    else:
        vencedor = "Empate"
        qtde = star_wars 

    print("\nResultado da votação:")
    print(f"Star Wars: {star_wars} votos")
    print(f"Star Trek: {star_trek} votos")
    print(f"Vencedor: {vencedor} ({qtde} votos)")


# nosso programa principal
registrar_votos()
apurar_votos()