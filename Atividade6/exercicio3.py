# Exercicio 3 - Consulta de CEP via ViaCEP
# Retorna logradouro, bairro, cidade e estado

import json
import urllib.request
import urllib.error
import re


def consultar_cep(cep: str, timeout=10):
    # Normaliza: manter apenas dígitos
    cep_digits = re.sub(r"\D", "", cep)
    if len(cep_digits) != 8:
        raise ValueError("CEP inválido. Deve conter 8 dígitos.")

    url = f"https://viacep.com.br/ws/{cep_digits}/json/"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = resp.read()
            obj = json.loads(data)
    except urllib.error.URLError:
        raise ConnectionError("Falha na conexão com a API ViaCEP")
    except Exception as e:
        raise RuntimeError(f"Erro ao processar resposta: {e}")

    if obj.get("erro"):
        raise LookupError("CEP não encontrado")

    return {
        "logradouro": obj.get("logradouro", ""),
        "bairro": obj.get("bairro", ""),
        "cidade": obj.get("localidade", ""),
        "estado": obj.get("uf", "")
    }


def main():
    print("Consulta CEP (ViaCEP)")
    cep = input("Digite o CEP (ex: 01001-000 ou 01001000): ")
    try:
        info = consultar_cep(cep)
    except ValueError as e:
        print(f"Erro: {e}")
        return
    except ConnectionError:
        print("Falha na conexão com a API. Tente novamente mais tarde.")
        return
    except LookupError:
        print("CEP não encontrado.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return

    print("--- Endereço ---")
    print(f"Logradouro: {info['logradouro']}")
    print(f"Bairro: {info['bairro']}")
    print(f"Cidade: {info['cidade']}")
    print(f"Estado: {info['estado']}")


if __name__ == "__main__":
    main()
