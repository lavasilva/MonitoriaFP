area = float(input("Digite a área do terreno para a classificação: "))

if 0 < area < 100:
    print("Classificação: Terreno Popular")
elif 100 <= area <= 500: # area <= 100 and area <= 500
    print("Classificação: Terreno Master")
else: 
    print("Classificação: Terreno VIP")