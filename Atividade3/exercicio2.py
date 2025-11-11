# Calculadora de IMC

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obeso"


def main():
    while True:
        try:
            peso = float(input("Digite o peso (kg): ").strip())
            altura = float(input("Digite a altura (m): ").strip())
        except ValueError:
            print("Entrada inválida. Informe números para peso e altura.")
            continue

        if altura <= 0:
            print("Altura deve ser maior que zero.")
            continue

        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc)

        print("=" * 50)
        print("CALCULADORA DE IMC")
        print("=" * 50)
        print(f"Peso: {peso:.2f} kg")
        print(f"Altura: {altura:.2f} m")
        print("-" * 50)
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("=" * 50)
        break


if __name__ == "__main__":
    main()
