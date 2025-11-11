# Exercicio 1 - calcular gorjeta

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """Retorna o valor da gorjeta.

    Args:
        valor_conta (float): valor total da conta
        porcentagem_gorjeta (float): porcentagem de gorjeta (ex: 10 para 10%)

    Returns:
        float: valor da gorjeta
    """
    if valor_conta < 0:
        raise ValueError("valor_conta não pode ser negativo")
    return valor_conta * (porcentagem_gorjeta / 100.0)


def main():
    while True:
        print("Calculadora de gorjeta")
        try:
            conta = float(input("Valor da conta: ").strip())
            porcent = float(input("Porcentagem de gorjeta (ex: 10): ").strip())
        except ValueError:
            print("Entrada inválida. Informe números.")
            continue

        gorjeta = calcular_gorjeta(conta, porcent)
        print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
        break


if __name__ == "__main__":
    main()
