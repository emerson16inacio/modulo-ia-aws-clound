# Registro de notas e cálculo da média da turma

def main():
    notas = []
    print("Digite as notas dos alunos. Aperte Enter sem digitar nada para finalizar.")

    while True:
        entrada = input("Nota (0-10): ").strip()
        if entrada == "":
            break
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. Informe um número (ex: 7.5).")
            continue

        if nota < 0 or nota > 10:
            print("Nota deve estar entre 0 e 10.")
            continue

        notas.append(nota)

    if not notas:
        print("Nenhuma nota registrada.")
        return

    media = sum(notas) / len(notas)
    print("\n--- RESULTADO ---")
    print(f"Quantidade de alunos: {len(notas)}")
    print(f"Média da turma: {media:.2f}")


if __name__ == "__main__":
    main()
