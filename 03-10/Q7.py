votos = [0, 0, 0, 0]
voto = -1

while voto != 0:
    voto = int(input("Informe seu voto (1=Windows Server, 2=Linux, 3=Mac OS, 4=Outro) ou 0 para encerrar: "))
    if voto == 1:
        votos[0] = votos[0] + 1
    elif voto == 2:
        votos[1] = votos[1] + 1
    elif voto == 3:
        votos[2] = votos[2] + 1
    elif voto == 4:
        votos[3] = votos[3] + 1

total_votos = votos[0] + votos[1] + votos[2] + votos[3]

vencedor = ""
max_votos = -1

if total_votos > 0:
    if votos[0] > max_votos:
        max_votos = votos[0]
        vencedor = "Windows Server"
    if votos[1] > max_votos:
        max_votos = votos[1]
        vencedor = "Linux"
    if votos[2] > max_votos:
        max_votos = votos[2]
        vencedor = "Mac OS"
    if votos[3] > max_votos:
        max_votos = votos[3]
        vencedor = "Outro"

    print("--- Resultado da Enquete ---")
    print(f"Total de votos para Windows Server: {votos[0]}")
    print(f"Total de votos para Linux: {votos[1]}")
    print(f"Total de votos para Mac OS: {votos[2]}")
    print(f"Total de votos para Outro: {votos[3]}")
    print(f"Total geral de votos: {total_votos}")
    print(f"O vencedor da votação é: {vencedor} com {max_votos} votos.")
else:
    print("Nenhum voto registrado.")