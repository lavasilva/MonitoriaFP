turma_a_qnt = 0
turma_b_qnt = 0
turma_c_qnt = 0
turma_d_qnt = 0

for i in range(10):
    nome = input("Digite seu nome: ")
    turma = input("Digite sua turma: [A] [B] [C] [D] ")

    if turma == "A":
        turma_a_qnt += 1
    elif turma == "B":
        turma_b_qnt += 1
    elif turma == "C":
        turma_c_qnt += 1
    elif turma == "D":
        turma_d_qnt += 1
    else:
        print("Essa turma não existe.")

turma_a_arrecadado = turma_a_qnt * 75.0
turma_b_arrecadado = turma_b_qnt * 58.0
turma_c_arrecadado = turma_c_qnt * 44.0
turma_d_arrecadado = turma_d_qnt * 50.0

print(f"""
Turma A - Quantidade: {turma_a_qnt}, Total Arrecadado: {turma_a_arrecadado}

Turma B - Quantidade: {turma_b_qnt}, Total Arrecadado: {turma_b_arrecadado}

Turma C - Quantidade: {turma_c_qnt}, Total Arrecadado: {turma_c_arrecadado}

Turma D - Quantidade: {turma_d_qnt}, Total Arrecadado: {turma_d_arrecadado}
""")