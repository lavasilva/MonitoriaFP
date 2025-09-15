repteis = []
mamiferos = []
aves = []
outros = []

for i in range(10):
    animal = input("Digite o nome do animal: ")
    categoria = int(input("Escolha a categoria (1-Réptil, 2-Mamífero, 3-Ave, 4-Outro): "))
    
    if categoria == 1:
        repteis.append(animal)
    elif categoria == 2:
        mamiferos.append(animal)
    elif categoria == 3:
        aves.append(animal)
    else:
        outros.append(animal)

print("Répteis:", repteis, "Quantidade:", len(repteis))
print("Mamíferos:", mamiferos, "Quantidade:", len(mamiferos))
print("Aves:", aves, "Quantidade:", len(aves))
print("Outros:", outros, "Quantidade:", len(outros))
