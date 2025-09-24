def validar_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:  # um IP precisa ter 4 partes
        return False
    for parte in partes:
        if not parte.isdigit():  # cada parte deve ser número
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:  # limite válido é 0 a 255 que é um byte
            return False
    return True


def main():
    nome_arquivo = "ips.txt"  

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            ip = linha.strip()  # remove espaços e quebras de linha
            if validar_ip(ip):
                print(f"{ip} -> Válido")
            else:
                print(f"{ip} -> Inválido")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")


if __name__ == "__main__":
    main()
