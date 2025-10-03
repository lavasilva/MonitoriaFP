#Escreva  um  programa  que  receba um valor em quilômetros e ofereça ao usuário 
#duas  opções  de  conversão:  converter  o  valor  em  metros  ou  em milhas. O programa 
#deverá chamar a função específica de conversão com base na escolha do usuário. A 
#função  para  converter  quilômetros  em  metros  deverá receber o valor em quilômetros 
#como  parâmetro  e  retornar  o  valor  equivalente  em  metros.  A  função  para  converter 
#quilômetros  em  milhas  deverá  receber  o  valor  em  quilômetros  e  retornar  o  valor 
#equivalente  em  milhas.  No  programa principal, imprima o valor retornado pela função 
#escolhida pelo usuário. 
  #Metros = km * 1000 
  #Milhas = Km * 0.62 

def km_para_metros(km):
    return km * 1000

def km_para_milhas(km):
    return km * 0.62

def main():
    km = float(input("Digite o valor em quilômetros: "))

    print("Escolha uma opção de conversão:")
    print("1 - Converter para metros")
    print("2 - Converter para milhas")

    opcao = input("Digite sua opção (1 ou 2): ")

    if opcao == "1":
        resultado = km_para_metros(km)
        print(f"{km} km equivalem a {resultado} metros.")
    elif opcao == "2":
        resultado = km_para_milhas(km)
        print(f"{km} km equivalem a {resultado} milhas.")
    else:
        print("Opção inválida!")

main()
