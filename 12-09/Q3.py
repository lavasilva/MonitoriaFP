A = []
B = []

for i in range(7):
    palavra = input("Digite uma palavra para a lista A: ")
    A.append(palavra)

for i in range(7):
    palavra = input("Digite uma palavra para a lista B: ")
    B.append(palavra)

A.append(B.pop(0))
# A.append(B(0))
# B.pop(0)

if "maçã" in B:
    print("A palavra 'maçã' está na lista B")
else:
    print("A palavra 'maçã' não está na lista B")

A.sort(reverse=True) 
B.sort(reverse=True)

print("Lista A:", A, "Tamanho:", len(A))
print("Lista B:", B, "Tamanho:", len(B))
