dia = input("Digite o dia de nascimento (DD): ")
mes = input("Digite o mês de nascimento (MM): ")
ano = input("Digite o ano de nascimento (AAAA): ")

dd_invertido = dia[::-1]
mm_invertido = mes[::-1]

senha = mes + "$" + dd_invertido + "#" + dia + "!" + mm_invertido + "*" + ano

print(f"Sua senha é: {senha}")