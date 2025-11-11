# Calculadora de Preço Total - Compra de Produtos

# Informações do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40  # R$
quantidade = 3

# Cálculo do preço total
# Preço Total = Preço Unitário × Quantidade
preco_total = preco_unitario * quantidade

# Exibição das informações
print("=" * 45)
print("CALCULADORA DE PREÇO TOTAL - COMPRA")
print("=" * 45)
print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print("-" * 45)
print(f"Preço Total: R$ {preco_total:.2f}")
print("=" * 45)
