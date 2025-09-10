notas = []

while True:
    nota = float(input("Digite uma nota (-1 para parar): "))
    
    if nota == -1:
        break
    
    notas.append(nota)

# a) Quantidade de notas digitadas
print("Quantidade de notas:", len(notas))

# b) Mostrar as notas maiores que 7.0
print("Notas maiores que 7.0:")
for n in notas:
    if n > 7.0:
        print(n)

# c) Calcular a média das notas
soma = 0
for n in notas:
    soma += n  
media = soma / len(notas)  
print("Média das notas:", media)

# d) Encontrar a menor e a maior nota
menor = notas[0]
maior = notas[0]

for n in notas:
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print("Menor nota:", menor)
print("Maior nota:", maior)

# e) Imprimir toda a lista com os índices
print("Lista de notas:")
i = 1 
for n in notas:
    print(i, n) 
    i += 1     
