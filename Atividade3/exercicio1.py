# Classificador de Idade

def classificar_idade(idade):
    if idade < 0:
        return None
    if idade <= 12:
        return "Criança"
    if 13 <= idade <= 17:
        return "Adolescente"
    if 18 <= idade <= 59:
        return "Adulto"
    return "Idoso"


def main():
    while True:
        try:
            entrada = input("Digite a idade (anos): ").strip()
            idade = int(entrada)
        except ValueError:
            print("Entrada inválida. Informe um número inteiro para a idade.")
            continue

        classificacao = classificar_idade(idade)
        if classificacao is None:
            print("Idade inválida (negativa).")
            continue
        print("=" * 40)
        print("CLASSIFICADOR DE IDADE")
        print("=" * 40)
        print(f"Idade: {idade} anos")
        print(f"Classificação: {classificacao}")
        print("=" * 40)
        break

if __name__ == "__main__":
    main()
