nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
frequencia = int(input("Frequencia: "))

if frequencia >= 75:
    media = (nota1 + nota2) / 2
    if media >= 7:
        print("Aprovado por média")
    else:
        print("Reprovado por média")
else:
    print("Reprovado por falta")