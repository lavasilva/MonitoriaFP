#Uma  pesquisa  foi  realizada  com  estudantes  de  uma  universidade.  Cada  participante 
#respondeu ao seguinte questionário: 
# Curso: Engenharia OU Direito 
#Você estuda em período integral? S OU N 
#Considere um arquivo (.txt ou .csv) onde as respostas de todos os participantes foram 
#armazenadas. As respostas foram organizadas da seguinte forma: um participante por 
#linha e suas respostas separadas por vírgulas. 
#Escreva  um  programa  que,  após  receber  as  respostas  de  5  participantes  por 
#input e escrever no arquivo, leia este arquivo e exiba as seguintes informações: 
 # ●  Quantos  estudantes  do  curso  de  Engenharia  estudam  em  período 
#integral? 
 # ●  Quantos  estudantes  não  estudam  em  período  integral, 
#independentemente do curso? 

def main():
    nome_arquivo = "pesquisa.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        print("Digite as respostas de 5 participantes:")

        for i in range(5):
            curso = input(f"Participante {i+1} - Curso (Engenharia ou Direito): ").strip()

            integral = input(f"Participante {i+1} - Estuda integralmente? (S/N): ").strip().upper()
            arquivo.write(curso + "," + integral + "\n")

    engenharia_integral = 0
    nao_integral = 0

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(",")
            if len(partes) != 2:
                continue

            curso = partes[0].strip().lower()  
            integral = partes[1].strip().upper() 

            if curso == "engenharia" and integral == "S":
                engenharia_integral += 1

            if integral == "N":
                nao_integral += 1

    print(f"\nQuantidade de estudantes de Engenharia em período integral: {engenharia_integral}")
    print(f"Quantidade de estudantes que NÃO estudam em período integral: {nao_integral}")


main()
