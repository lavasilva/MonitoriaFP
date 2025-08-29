level = int(input("Digite o level do Voltorb: "))

if 1 <= level <= 20:
    choque = 20 + (level ** 3)
elif 21 <= level <= 40:
    choque = 8000 + (level - 10) ** 2
elif 41 <= level <= 60:
    choque = 9000 + 5 * level
elif 61 <= level <= 80:
    choque = 9300 + 2 * level
elif 81 <= level <= 100:
    choque = 9500 + level

print(choque)