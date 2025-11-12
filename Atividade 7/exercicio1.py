import pandas as pd
import sys


def analisar_tempo_execucao(nome_arquivo: str) -> None:
	"""Lê um CSV e calcula média e desvio padrão da coluna 'tempo_execucao'.

	Exibe mensagens de erro caso o arquivo não exista ou a leitura falhe.
	"""
	try:
		df = pd.read_csv(nome_arquivo)
	except FileNotFoundError:
		print(f"ERRO: arquivo '{nome_arquivo}' não encontrado.")
		return
	except pd.errors.EmptyDataError:
		print(f"ERRO: arquivo '{nome_arquivo}' está vazio.")
		return
	except pd.errors.ParserError:
		print(f"ERRO: falha ao interpretar o CSV '{nome_arquivo}'. Verifique o formato.")
		return
	except Exception as e:
		print(f"ERRO inesperado ao abrir '{nome_arquivo}': {e}")
		return

	if 'tempo_execucao' not in df.columns:
		print("ERRO: coluna 'tempo_execucao' não encontrada no CSV.")
		return

	try:
		serie = pd.to_numeric(df['tempo_execucao'], errors='coerce')
		serie = serie.dropna()
		if len(serie) == 0:
			print("ERRO: não há valores numéricos válidos na coluna 'tempo_execucao'.")
			return

		media = serie.mean()
		desvio = serie.std()
		print(f"Arquivo: {nome_arquivo}")
		print(f"Média (tempo_execucao): {media:.4f}")
		print(f"Desvio padrão (tempo_execucao): {desvio:.4f}")
	except Exception as e:
		print(f"ERRO ao calcular estatísticas: {e}")


def main():
	# permite passar o arquivo como argumento ou pedir interativamente
	if len(sys.argv) >= 2:
		caminho = sys.argv[1]
	else:
		caminho = input('Caminho para o arquivo CSV: ').strip()

	if not caminho:
		print('Nenhum arquivo informado. Encerrando.')
		return

	analisar_tempo_execucao(caminho)


if __name__ == '__main__':
	main()

