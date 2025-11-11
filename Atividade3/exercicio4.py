# Verificador de Ano Bissexto

def eh_bissexto(ano):
    # Divisível por 4 e (não divisível por 100 ou divisível por 400)
    return (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))


def main():
    while True:
        try:
            ano = int(input("Digite o ano (ex: 2024): ").strip())
        except ValueError:
            print("Entrada inválida. Informe um ano inteiro.")
            continue

        resultado = eh_bissexto(ano)

        print("=" * 40)
        print("VERIFICADOR DE ANO BISSEXTO")
        print("=" * 40)
        print(f"Ano: {ano}")
        print(f"É bissexto? {'Sim' if resultado else 'Não'}")
        print("=" * 40)
        break


if __name__ == "__main__":
    main()
