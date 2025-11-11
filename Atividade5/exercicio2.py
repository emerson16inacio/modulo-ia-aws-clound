# Exercicio 2 - verificação de palíndromo

import re


def eh_palindromo(texto: str) -> bool:
    """Verifica se o texto é palíndromo, ignorando espaços e pontuação."""
    # Remove caracteres não alfanuméricos e transforma em minúsculas
    limp = re.sub(r"[^A-Za-z0-9]", "", texto).lower()
    return limp == limp[::-1]


def main():
    s = input("Digite uma palavra ou frase: ")
    if eh_palindromo(s):
        print("Essa frase ou palavra é palíndromo.")
    else:
        print("Não é palíndromo.")



if __name__ == "__main__":
    main()
