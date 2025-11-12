# Exercicio 4 - Consultar câmbio em relação ao BRL usando AwesomeAPI
# Mostra valor atual (bid), máxima, mínima e data/hora da última atualização

import json
import urllib.request
import urllib.error


API_BASE = "https://economia.awesomeapi.com.br/json/last/"


def consultar_cambio(consulta_moeda: str, timeout=10):
    moeda = consulta_moeda.strip().upper()
    if not moeda:
        raise ValueError("Código de moeda inválido")

    pair = f"{moeda}-BRL"
    url = API_BASE + pair
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = resp.read()
            obj = json.loads(data)
    except urllib.error.URLError:
        raise ConnectionError("Falha na conexão com a API de câmbio")
    except Exception as e:
        raise RuntimeError(f"Erro ao processar resposta: {e}")

    key = moeda + "BRL"
    if key not in obj:
        raise LookupError("Moeda não encontrada ou não suportada")

    info = obj[key]
    # Campos: bid (valor atual), high, low, create_date
    return {
        "valor_atual": info.get("bid"),
        "maxima": info.get("high"),
        "minima": info.get("low"),
        "ultima_atualizacao": info.get("create_date")
    }


def main():
    print("Consulta de câmbio (ex: USD, EUR)")
    moeda = input("Digite o código da moeda a ser consultada em relação ao BRL: ")
    try:
        resp = consultar_cambio(moeda)
    except ValueError as e:
        print(f"Erro: {e}")
        return
    except ConnectionError:
        print("Falha na conexão com a API. Verifique sua internet.")
        return
    except LookupError:
        print("Moeda não encontrada ou não suportada pela API.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    print("--- Resultado ---")
    print(f"Valor atual: {resp['valor_atual']}")
    print(f"Máxima: {resp['maxima']}")
    print(f"Mínima: {resp['minima']}")
    print(f"Última atualização: {resp['ultima_atualizacao']}")


if __name__ == "__main__":
    main()
