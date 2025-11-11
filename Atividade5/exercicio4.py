# Exercicio 4 - calcular quantos dias uma pessoa está viva

from datetime import datetime, date


def dias_vivo(data_nascimento: date, referencia: date | None = None) -> int:
    """Retorna a quantidade de dias vividos desde a data_nascimento até a data referencia (ou hoje)."""
    if referencia is None:
        referencia = date.today()
    if data_nascimento > referencia:
        raise ValueError("Data de nascimento não pode ser no futuro")
    delta = referencia - data_nascimento
    return delta.days


def parse_data(entrada: str) -> date:
    """Tenta parsear formatos comuns: YYYY-MM-DD, DD/MM/YYYY, DD-MM-YYYY."""
    entrada = entrada.strip()
    formatos = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]
    for fmt in formatos:
        try:
            return datetime.strptime(entrada, fmt).date()
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use YYYY-MM-DD ou DD/MM/YYYY")


def main():
    print("Calculadora de dias vividos")
    s = input("Digite sua data de nascimento (YYYY-MM-DD ou DD/MM/YYYY): ")
    try:
        dn = parse_data(s)
        dias = dias_vivo(dn)
    except ValueError as e:
        print(f"Erro: {e}")
        return

    print(f"Você está vivo(a) há {dias} dias.")


if __name__ == "__main__":
    main()
