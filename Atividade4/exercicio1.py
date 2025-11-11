# Calculadora simples - operações básicas

def main():
    while True:
        print("\n--- CALCULADORA ---")
        print("1) Soma (+)")
        print("2) Subtração (-)")
        print("3) Multiplicação (*)")
        print("4) Divisão (/)")
        print("0) Sair")

        opc = input("Escolha uma opção (0-4): ").strip()
        if opc == "0":
            print("Encerrando calculadora.")
            break

        if opc not in {"1", "2", "3", "4"}:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            a = float(input("Digite o primeiro número: ").strip())
            b = float(input("Digite o segundo número: ").strip())
        except ValueError:
            print("Entrada inválida. Informe números.")
            continue

        if opc == "1":
            resultado = a + b
            simbolo = "+"
        elif opc == "2":
            resultado = a - b
            simbolo = "-"
        elif opc == "3":
            resultado = a * b
            simbolo = "*"
        else:  # opc == "4"
            if b == 0:
                print("Erro: divisão por zero não é permitida.")
                continue
            resultado = a / b
            simbolo = "/"

        print(f"{a} {simbolo} {b} = {resultado}")


if __name__ == "__main__":
    main()
