area = float(input("Digite a área do terreno para a classificação: "))

if 0 < area < 100:
    print("Classificação: Terreno Popular")
elif area >= 100 or area <= 500:
    print("Classificação: Terreno Master")
else: 
    print("Classificação: Terreno VIP")