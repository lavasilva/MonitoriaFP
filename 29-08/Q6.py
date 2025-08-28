nome = str(input("Boa noite! Nos informe seu nome: "))
s1 = float(input("\nDigite seu salário atual para checarmos a possibilidade de reajuste: "))

if 0 < s1 <= 999.99:
    dependentes = str(input("Você possui dependentes? Responda com S ou N: "))

    if dependentes == 'S':
        s2 = s1 + (0.25 * s1) # salario + 25% do valor
    else:
        s2 = s1 + (0.20 * s1) # salario + 20% do valor

elif 1000.00 <= s1 <= 5000.00:
    s2 = s1 + (0.1 * s1) # salario + 10% do valor

else:
    s2 = s1

print("Jogador: ", nome)
print("Salário inicial: ", s1)
print("Salário final: ", s2)