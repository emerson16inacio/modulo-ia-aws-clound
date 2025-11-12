# Exercicio 1 - Gerador de senhas seguras
# Gera senhas com letras, números e símbolos; usuário escolhe o tamanho

import secrets
import string
import random


def gerar_senha(tamanho: int, usar_minusculas=True, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True) -> str:
    if tamanho <= 0:
        raise ValueError("Tamanho deve ser positivo")

    categorias = []
    if usar_minusculas:
        categorias.append(string.ascii_lowercase)
    if usar_maiusculas:
        categories_upper = string.ascii_uppercase
        categorias.append(categories_upper)
    if usar_numeros:
        categorias.append(string.digits)
    if usar_simbolos:
        # símbolos seguros para senhas
        categorias.append("!@#$%&*()-_=+[]{};:,.<>?/")

    if not categorias:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")

    # Garantir que a senha contenha pelo menos um caractere de cada categoria selecionada
    senha_chars = [secrets.choice(cat) for cat in categorias]

    # Constroi o pool total
    pool = "".join(categorias)

    # Preencher o restante da senha
    while len(senha_chars) < tamanho:
        senha_chars.append(secrets.choice(pool))

    # Embaralhar de forma segura
    random.SystemRandom().shuffle(senha_chars)
    return "".join(senha_chars)


def main():
    print("Gerador de senhas seguras")
    try:
        tamanho = int(input("Qual o tamanho da senha desejada? (ex: 12): ").strip())
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    # Perguntar se usuário quer opções (padrão todas ativas)
    opc = input("Deseja incluir maiúsculas? [S/n] (padrão S): ").strip().lower()
    usar_maius = (opc != "n")
    opc = input("Deseja incluir minúsculas? [S/n] (padrão S): ").strip().lower()
    usar_minus = (opc != "n")
    opc = input("Deseja incluir números? [S/n] (padrão S): ").strip().lower()
    usar_num = (opc != "n")
    opc = input("Deseja incluir símbolos? [S/n] (padrão S): ").strip().lower()
    usar_sim = (opc != "n")

    try:
        senha = gerar_senha(tamanho, usar_minusculas=usar_minus, usar_maiusculas=usar_maius, usar_numeros=usar_num, usar_simbolos=usar_sim)
    except ValueError as e:
        print(f"Erro: {e}")
        return

    print(f"Senha gerada: {senha}")


if __name__ == "__main__":
    main()
