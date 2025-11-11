# Exercicio 3 - cálculo de desconto e preço final

def calcular_valor_desconto(preco: float, porcentagem: float) -> float:
    """Retorna o valor do desconto."""
    if preco < 0:
        raise ValueError("Preço não pode ser negativo")
    return preco * (porcentagem / 100.0)


def calcular_preco_final(preco: float, porcentagem: float) -> float:
    """Retorna o preço final após aplicar o desconto."""
    desconto = calcular_valor_desconto(preco, porcentagem)
    return preco - desconto


def main():
    print("Cálculo de desconto")
    try:
        preco = float(input("Preço do produto: R$ ").strip())
        porcent = float(input("Porcentagem de desconto (ex: 15): ").strip())
    except ValueError:
        print("Entrada inválida. Informe números.")
        return

    preco_final = calcular_preco_final(preco, porcent)
    print(f"Preço final: R$ {preco_final:.2f}")


if __name__ == "__main__":
    main()
