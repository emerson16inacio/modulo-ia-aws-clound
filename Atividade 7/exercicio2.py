"""
Exercicio 2 - Criar um arquivo CSV com nome, idade e cidade de algumas pessoas.
O programa pede o nome do arquivo ao usuário e salva os dados em formato tabular.
Trata erros ao salvar.
"""

import csv


def main():
    pessoas = [
        {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
        {"nome": "Bruno", "idade": 35, "cidade": "Rio de Janeiro"},
        {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"},
    ]

    arquivo = input('Nome do arquivo para salvar (ex: pessoas.csv): ').strip()
    if not arquivo:
        print('Nome de arquivo não informado.')
        return

    try:
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['nome', 'idade', 'cidade']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in pessoas:
                writer.writerow(p)
    except OSError as e:
        print(f'Falha ao salvar o arquivo: {e}')
        return

    print(f'Arquivo salvo com sucesso em: {arquivo}')


if __name__ == '__main__':
    main()
