"""
Exercicio 4 - Ler e escrever arquivo JSON contendo dicionário/lista com nome, idade e cidade.
Salva os dados em um arquivo escolhido pelo usuário e depois lê o mesmo arquivo exibindo os dados.
Trata erros de leitura/escrita.
"""

import json


def main():
    pessoas = [
        {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
        {"nome": "Bruno", "idade": 35, "cidade": "Rio de Janeiro"},
        {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"},
    ]

    arquivo = input('Nome do arquivo JSON para salvar (ex: pessoas.json): ').strip()
    if not arquivo:
        print('Nome de arquivo não informado.')
        return

    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(pessoas, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f'Falha ao salvar o arquivo: {e}')
        return

    print(f'Arquivo salvo com sucesso em: {arquivo}\nAgora lendo o arquivo...')

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('Erro: arquivo não encontrado ao tentar ler.')
        return
    except json.JSONDecodeError as e:
        print(f'Erro ao decodificar JSON: {e}')
        return
    except OSError as e:
        print(f'Erro ao ler o arquivo: {e}')
        return

    print('--- Dados lidos ---')
    for p in data:
        print(f"Nome: {p.get('nome')}, Idade: {p.get('idade')}, Cidade: {p.get('cidade')}")


if __name__ == '__main__':
    main()
