# Exercicio 2 - Buscar usuário aleatório via API (randomuser.me)
# Mostra nome, e-mail e país; trata erros de conexão

import json
import urllib.request
import urllib.error


API_URL = "https://randomuser.me/api/"


def buscar_usuario_aleatorio(timeout=10):
    try:
        with urllib.request.urlopen(API_URL, timeout=timeout) as resp:
            data = resp.read()
            obj = json.loads(data)
    except urllib.error.URLError:
        raise ConnectionError("Falha na conexão com a API")
    except Exception as e:
        raise RuntimeError(f"Erro ao processar resposta: {e}")

    if "results" not in obj or not obj["results"]:
        raise RuntimeError("Resposta inválida da API")

    r = obj["results"][0]
    nome = "{} {}".format(r.get("name", {}).get("first", ""), r.get("name", {}).get("last", "")).strip()
    email = r.get("email", "")
    pais = r.get("location", {}).get("country", "")
    return {"nome": nome, "email": email, "pais": pais}


def main():
    print("Busca de usuário aleatório (API)")
    try:
        u = buscar_usuario_aleatorio()
    except ConnectionError:
        print("Falha na conexão. Verifique sua internet e tente novamente.")
        return
    except Exception as e:
        print(f"Erro: {e}")
        return

    print("--- Usuário obtido ---")
    print(f"Nome: {u['nome']}")
    print(f"E-mail: {u['email']}")
    print(f"País: {u['pais']}")


if __name__ == "__main__":
    main()
