# Calculadora de Média Escolar

# Notas do aluno
nota1 = 8.5
nota2 = 7.0
nota3 = 9.5
nota4 = 8.0

# Cálculo da média aritmética
# Média = (Nota1 + Nota2 + Nota3 + Nota4) / 4
media = (nota1 + nota2 + nota3 + nota4) / 4

# Determinação da situação do aluno
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Exibição dos resultados
print("=" * 50)
print("CALCULADORA DE MÉDIA ESCOLAR")
print("=" * 50)
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Nota 4: {nota4}")
print("-" * 50)
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
print("=" * 50)
