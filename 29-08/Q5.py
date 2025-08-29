opcao = input("Digite 'C' para converter para Celsius ou 'F' para converter para Fahrenheit: ").upper()

temperatura = float(input("Digite a temperatura: "))

if opcao == "F":
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado:.2f}°F")
elif opcao == "C":
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado:.2f}°C")
else:
    print("Opção inválida! Digite apenas 'C' ou 'F'.")