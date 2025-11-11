# Classificação de números: pares ou ímpares

def main():
    pares = []
    impares = []

    print("Digite números inteiros. Aperte Enter sem digitar nada para finalizar.")
    while True:
        entrada = input("Número inteiro: ").strip()
        if entrada == "":
            break
        try:
            n = int(entrada)
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")
            continue

        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("\n---- RESUMO ----")
    print(f"Total de números: {len(pares) + len(impares)}")
    print(f"Pares ({len(pares)}): {pares}")
    print(f"Ímpares ({len(impares)}): {impares}")


if __name__ == "__main__":
    main()
