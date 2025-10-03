total_pessoas_cao = 0
soma_idades_gato = 0
qnt_pessoas_gato = 0

for i in range(5):
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    adocao = input("Digite o animal que você deseja adotar: [Cão] [Gato] [N/A] ")

    if adocao == "Cão":
        total_pessoas_cao += 1

    if adocao == "Gato":
        qnt_pessoas_gato += 1
        soma_idades_gato += idade

media = soma_idades_gato / qnt_pessoas_gato

print("Total de Pessoas que desejam adotar um Cachorro: ", total_pessoas_cao)
print(f"Media da Idade das pessoas que desejam adotar um Gato: {media:.2f}")