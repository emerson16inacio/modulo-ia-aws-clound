# Conversor de Moeda - Reais para Dólares e Euros

# Dados de entrada
valor_reais = 100.00  # R$
taxa_dolar = 5.20    # R$ por dólar
taxa_euro = 6.15     # R$ por euro

# Cálculos de conversão
# Valor em dólares = Valor em reais / Taxa do dólar
valor_dolares = valor_reais / taxa_dolar

# Valor em euros = Valor em reais / Taxa do euro
valor_euros = valor_reais / taxa_euro

# Exibição dos resultados
print("=" * 50)
print("CONVERSOR DE MOEDA - REAIS PARA DÓLARES E EUROS")
print("=" * 50)
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print("-" * 50)
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Valor em Dólares: USD $ {valor_dolares:.2f}")
print("-" * 50)
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print(f"Valor em Euros: EUR € {valor_euros:.2f}")
print("=" * 50)
