"""
Exercicio 3 - Ler um arquivo texto informado pelo usuário e exibir cada linha.
Caso o arquivo não seja encontrado, exibir mensagem de erro.
"""


def main():
    caminho = input('Digite o caminho do arquivo de texto: ').strip()
    if not caminho:
        print('Nenhum caminho informado.')
        return

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for i, linha in enumerate(f, start=1):
                print(f'{i:03d}: {linha.rstrip()}')
    except FileNotFoundError:
        print('Erro: arquivo não encontrado.')
    except OSError as e:
        print(f'Erro ao ler o arquivo: {e}')


if __name__ == '__main__':
    main()
