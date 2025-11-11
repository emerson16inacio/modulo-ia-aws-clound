# Verificação básica de segurança de senha


def tem_numero(senha: str) -> bool:
    return any(c.isdigit() for c in senha)


def main():
    print("Requisitos: pelo menos 8 caracteres e pelo menos 1 número.")
    while True:
        senha = input("Digite a senha: ")

        if len(senha) < 8:
            print("Senha muito curta. Deve ter pelo menos 8 caracteres.")
            continue

        if not tem_numero(senha):
            print("Senha precisa conter pelo menos um número.")
            continue

        print("Senha atende aos requisitos básicos de segurança.")
        break


if __name__ == "__main__":
    main()
