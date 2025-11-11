# Conversor de Temperatura


def c_para_f(c):
    return (c * 9/5) + 32


def c_para_k(c):
    return c + 273.15


def f_para_c(f):
    return (f - 32) * 5/9


def f_para_k(f):
    return c_para_k(f_para_c(f))


def k_para_c(k):
    return k - 273.15


def k_para_f(k):
    return c_para_f(k_para_c(k))


def convert(temperature, origem, destino):
    origem = origem.upper()
    destino = destino.upper()
    if origem == destino:
        return temperature

    if origem == 'C':
        if destino == 'F':
            return c_para_f(temperature)
        if destino == 'K':
            return c_para_k(temperature)
    if origem == 'F':
        if destino == 'C':
            return f_para_c(temperature)
        if destino == 'K':
            return f_para_k(temperature)
    if origem == 'K':
        if destino == 'C':
            return k_para_c(temperature)
        if destino == 'F':
            return k_para_f(temperature)

    return None


def main():
    while True:
        try:
            temp = float(input("Digite a temperatura: ").strip())
        except ValueError:
            print("Temperatura inválida.")
            continue

        origem = input("Unidade de origem (C/F/K): ").strip().upper()
        destino = input("Unidade destino (C/F/K): ").strip().upper()

        if origem not in ('C','F','K') or destino not in ('C','F','K'):
            print("Unidade inválida. Use C, F ou K.")
            continue

        resultado = convert(temp, origem, destino)
        if resultado is None:
            print("Conversão não suportada.")
            continue

        print("=" * 60)
        print("CONVERSOR DE TEMPERATURA")
        print("=" * 60)
        print(f"Temperatura origem: {temp:.2f} {origem}")
        print(f"Unidade destino: {destino}")
        print("-" * 60)
        print(f"Resultado: {resultado:.2f} {destino}")
        print("=" * 60)
        break


if __name__ == "__main__":
    main()
