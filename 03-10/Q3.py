while True:
    botao1 = int(input("Digite o numero do botão 1: "))
    botao2 = int(input("Digite o numero do botão 2: "))
    break

soma = botao1 + botao2

if soma == 0:
    print("0 - PROXYCITY")
elif soma == 1:
    print("1 - P.Y.N.G.")
elif soma == 2:
    print("2 - DNSUEY!")
elif soma == 3:
    print("3 - SERVERS")
elif soma == 4:
    print("4 - HOST!")
elif soma == 5:
    print("5 - CRIPTONIZE")
elif soma == 6:
    print("6 - OFFLINE DAY")
elif soma == 7:
    print("7 - SALT")
else:
    print("Não existe música com esse valor.")