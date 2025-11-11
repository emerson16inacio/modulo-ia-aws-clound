# Calculadora de Desconto

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00  # R$
percentual_desconto = 20  # %

# Cálculos
# Valor do desconto = Preço original × (Percentual de desconto / 100)
valor_desconto = preco_original * (percentual_desconto / 100)

# Preço final = Preço original - Valor do desconto
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("=" * 50)
print("CALCULADORA DE DESCONTO")
print("=" * 50)
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Percentual de Desconto: {percentual_desconto}%")
print("-" * 50)
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print("=" * 50)
