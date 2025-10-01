lista_numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista_numeros.append(numero)

limite_inferior = int(input("Limite inferior: "))
limite_superior = int(input("Limite superior: "))

nova_lista = []

for elemento in lista_numeros:
    if elemento >= limite_inferior and elemento <= limite_superior:
        nova_lista.append(elemento)

print(f"Nova lista: {nova_lista}")