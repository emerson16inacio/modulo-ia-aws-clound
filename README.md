# Módulo IA AWS Cloud - Exercícios Python

Repositório contendo 7 atividades práticas de Python, abrangendo desde conceitos básicos até programação com APIs externas e manipulação de arquivos.

---

## 📋 Índice

- [Atividade 1](#atividade-1-operações-básicas)
- [Atividade 2](#atividade-2-estruturas-de-dados)
- [Atividade 3](#atividade-3-validação-e-entrada)
- [Atividade 4](#atividade-4-funções-e-tratamento-de-erros)
- [Atividade 5](#atividade-5-manipulação-de-dados)
- [Atividade 6](#atividade-6-integração-com-apis)
- [Atividade 7](#atividade-7-manipulação-de-arquivos)
- [Requisitos](#requisitos)
- [Como Usar](#como-usar)

---

## Atividade 1: Operações Básicas

### Exercício 1 - Calculadora com Operações Básicas
**Descrição:** Cria uma calculadora interativa que realiza operações aritméticas básicas (+, -, *, /).

**Recursos:**
- Menu interativo com escolha de operação
- Tratamento de entradas inválidas
- Validação de divisão por zero
- Loop contínuo até opção de sair

**Como usar:**
```bash
python3 "Atividade1/exercicio1.py"
```

### Exercício 2 - Registro de Notas e Cálculo de Média
**Descrição:** Registra notas de alunos e calcula a média da turma.

**Recursos:**
- Entrada interativa de notas (0-10)
- Validação de intervalo
- Cálculo de média
- Encerramento com Enter vazio

**Como usar:**
```bash
python3 "Atividade1/exercicio2.py"
```

### Exercício 3 - Verificação de Segurança de Senha
**Descrição:** Verifica se uma senha atende a critérios básicos de segurança.

**Critérios validados:**
- Mínimo de 8 caracteres
- Ao menos um número

**Como usar:**
```bash
python3 "Atividade1/exercicio3.py"
```

### Exercício 4 - Classificação de Números (Par/Ímpar)
**Descrição:** Analisa números digitados pelo usuário e os classifica como pares ou ímpares.

**Recursos:**
- Entrada interativa de números inteiros
- Classificação automática
- Contagem total de pares e ímpares
- Exibição de listas separadas

**Como usar:**
```bash
python3 "Atividade1/exercicio4.py"
```

---

## Atividade 2: Estruturas de Dados

### Exercício 1 - [Descrição do exercicio1]
**Descrição:** Trabalha com estruturas de dados.

**Como usar:**
```bash
python3 "Atividade2/exercicio1.py"
```

### Exercício 2 - [Descrição do exercicio2]
**Descrição:** Manipulação de dados.

**Como usar:**
```bash
python3 "Atividade2/exercicio2.py"
```

### Exercício 3 - [Descrição do exercicio3]
**Descrição:** Operações com coleções.

**Como usar:**
```bash
python3 "Atividade2/exercicio3.py"
```

### Exercício 4 - [Descrição do exercicio4]
**Descrição:** Processamento de dados.

**Como usar:**
```bash
python3 "Atividade2/exercicio4.py"
```

---

## Atividade 3: Validação e Entrada

### Exercício 1 - [Descrição do exercicio1]
**Descrição:** Validação de entradas do usuário.

**Como usar:**
```bash
python3 "Atividade3/exercicio1.py"
```

### Exercício 2 - Calculadora de IMC com Loop Infinito
**Descrição:** Calcula o Índice de Massa Corporal (IMC) e classifica o resultado.

**Recursos:**
- Loop infinito até entrada válida
- Cálculo de IMC (peso / altura²)
- Classificação automática:
  - Abaixo do peso (IMC < 18.5)
  - Peso normal (18.5 ≤ IMC < 25)
  - Sobrepeso (25 ≤ IMC < 30)
  - Obeso (IMC ≥ 30)
- Tratamento de erros de entrada
- Validação de altura > 0

**Como usar:**
```bash
python3 "Atividade3/exercicio2.py"
```

### Exercício 3 - [Descrição do exercicio3]
**Descrição:** Validação avançada.

**Como usar:**
```bash
python3 "Atividade3/exercicio3.py"
```

### Exercício 4 - [Descrição do exercicio4]
**Descrição:** Processamento com validação.

**Como usar:**
```bash
python3 "Atividade3/exercicio4.py"
```

---

## Atividade 4: Funções e Tratamento de Erros

### Exercício 1 - Calculadora Interativa
**Descrição:** Calculadora com menu interativo e operações básicas.

**Recursos:**
- Menu de seleção (1-4 para operações, 0 para sair)
- Entrada interativa de números
- Tratamento de divisão por zero
- Validação de opção

**Como usar:**
```bash
python3 "Atividade4/exercicio1.py"
```

### Exercício 2 - Registro e Média de Notas
**Descrição:** Registra notas de alunos e calcula a média.

**Recursos:**
- Entrada interativa de notas
- Cálculo de média da turma
- Encerramento com Enter vazio
- Quantidade de alunos registrados

**Como usar:**
```bash
python3 "Atividade4/exercicio2.py"
```

### Exercício 3 - Verificação de Senha Segura
**Descrição:** Valida senhas com critérios de segurança.

**Critérios:**
- Mínimo 8 caracteres
- Ao menos um número

**Como usar:**
```bash
python3 "Atividade4/exercicio3.py"
```

### Exercício 4 - Classificação de Números
**Descrição:** Classifica números como pares ou ímpares com contagem.

**Recursos:**
- Entrada iterativa de números
- Classificação automática
- Listas separadas por tipo
- Contagem total

**Como usar:**
```bash
python3 "Atividade4/exercicio4.py"
```

---

## Atividade 5: Manipulação de Dados

### Exercício 1 - Cálculo de Gorjeta
**Descrição:** Calcula o valor da gorjeta baseado na conta total e porcentagem desejada.

**Função principal:**
```python
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float
```

**Parâmetros:**
- `valor_conta`: Valor total da conta em reais
- `porcentagem_gorjeta`: Porcentagem (ex: 10 para 10%)

**Retorno:** Valor da gorjeta calculado

**Como usar:**
```bash
python3 "Atividade5/exercicio1.py"
```

### Exercício 2 - Validação de Palíndromo
**Descrição:** Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente).

**Recursos:**
- Ignora espaços em branco
- Ignora pontuação
- Case-insensitive
- Retorna "Sim" ou "Não"

**Exemplos:**
- "ama" → Sim
- "A man, a plan, a canal: Panama" → Sim
- "Python" → Não

**Como usar:**
```bash
python3 "Atividade5/exercicio2.py"
```

### Exercício 3 - Cálculo de Desconto
**Descrição:** Calcula o preço final de um produto após aplicar desconto percentual.

**Recursos:**
- Cálculo de valor do desconto
- Preço final após desconto
- Formatação para 2 casas decimais (centavos)
- Interação interativa com usuário

**Como usar:**
```bash
python3 "Atividade5/exercicio3.py"
```

### Exercício 4 - Cálculo de Dias Vividos
**Descrição:** Calcula quantos dias uma pessoa está viva baseado na data de nascimento.

**Recursos:**
- Aceita formatos de data: YYYY-MM-DD e DD/MM/YYYY
- Validação de data de nascimento
- Cálculo de dias até hoje
- Tratamento de erros

**Como usar:**
```bash
python3 "Atividade5/exercicio4.py"
# Digite sua data de nascimento (ex: 1995-05-15 ou 15/05/1995)
```

---

## Atividade 6: Integração com APIs

### Exercício 1 - Gerador de Senhas Seguras
**Descrição:** Gera senhas aleatórias com letras, números e símbolos.

**Recursos:**
- Tamanho customizável
- Opções de incluir/excluir: maiúsculas, minúsculas, números, símbolos
- Uso de `secrets` para segurança criptográfica
- Embaralhamento seguro

**Como usar:**
```bash
python3 "Atividade6/exercicio1.py"
```

### Exercício 2 - Busca de Usuário Aleatório
**Descrição:** Busca um usuário fictício aleatório via API randomuser.me.

**Recursos:**
- Integração com API REST
- Exibe: nome, e-mail e país
- Tratamento de erros de conexão
- Mensagem de falha se API não responder

**API utilizada:** https://randomuser.me/api/

**Como usar:**
```bash
python3 "Atividade6/exercicio2.py"
```

### Exercício 3 - Consulta de CEP
**Descrição:** Consulta informações de endereço a partir de um CEP via API ViaCEP.

**Retorna:**
- Logradouro
- Bairro
- Cidade
- Estado

**Recursos:**
- Validação de formato de CEP
- Aceita formatos: 01001-000 ou 01001000
- Tratamento de CEP não encontrado
- Mensagem de erro para falhas

**API utilizada:** https://viacep.com.br/ws/{cep}/json/

**Como usar:**
```bash
python3 "Atividade6/exercicio3.py"
# Digite o CEP (ex: 01001-000 ou 01001000)
```

### Exercício 4 - Consulta de Taxa de Câmbio
**Descrição:** Consulta a taxa de câmbio de uma moeda em relação ao BRL (Real).

**Exibe:**
- Valor atual (bid)
- Valor máximo
- Valor mínimo
- Data e hora da última atualização

**Recursos:**
- Suporta múltiplas moedas (USD, EUR, GBP, etc.)
- Tratamento de moeda não encontrada
- Mensagem de erro para falhas de conexão

**API utilizada:** https://economia.awesomeapi.com.br/json/last/

**Como usar:**
```bash
python3 "Atividade6/exercicio4.py"
# Digite o código da moeda (ex: USD, EUR, GBP)
```

---

## Atividade 7: Manipulação de Arquivos

### Exercício 1 - Análise de CSV com Pandas
**Descrição:** Lê um arquivo CSV e calcula média e desvio padrão da coluna `tempo_execucao`.

**Recursos:**
- Utiliza pandas para processamento de dados
- Calcula média (mean)
- Calcula desvio padrão (std)
- Tratamento de erros:
  - Arquivo não encontrado
  - Arquivo vazio
  - CSV mal formatado
  - Coluna não existe
  - Valores não numéricos

**Formato esperado do CSV:**
```
tempo_execucao
1.2
2.5
3.0
2.8
1.9
```

**Como usar:**
```bash
python3 "Atividade7/exercicio1.py"
# Digite o caminho do arquivo CSV (ex: sample_tempo.csv)
```

### Exercício 2 - Criação de Arquivo CSV
**Descrição:** Cria um arquivo CSV com dados de pessoas (nome, idade, cidade).

**Recursos:**
- Gera dados de exemplo
- Formato tabular (CSV)
- Usuário escolhe o nome do arquivo
- Tratamento de erros ao salvar

**Dados de exemplo:**
- Ana, 28 anos, São Paulo
- Bruno, 35 anos, Rio de Janeiro
- Carla, 22 anos, Belo Horizonte

**Como usar:**
```bash
python3 "Atividade7/exercicio2.py"
# Digite o nome do arquivo (ex: pessoas.csv)
```

### Exercício 3 - Leitura de Arquivo de Texto
**Descrição:** Lê um arquivo de texto linha por linha e exibe na tela.

**Recursos:**
- Entrada interativa do caminho do arquivo
- Numeração de linhas
- Tratamento de arquivo não encontrado
- Exibição formatada

**Como usar:**
```bash
python3 "Atividade7/exercicio3.py"
# Digite o caminho do arquivo de texto
```

### Exercício 4 - Manipulação de JSON
**Descrição:** Salva dados em JSON e depois lê o mesmo arquivo exibindo os dados.

**Recursos:**
- Salva dicionários/listas em JSON
- Formato estruturado com identação
- Leitura posterior dos dados salvos
- Tratamento de erros:
  - Arquivo não existe
  - Erro ao decodificar JSON
  - Falha ao salvar

**Dados de exemplo:**
```json
[
  {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
  {"nome": "Bruno", "idade": 35, "cidade": "Rio de Janeiro"},
  {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"}
]
```

**Como usar:**
```bash
python3 "Atividade7/exercicio4.py"
# Digite o nome do arquivo JSON (ex: pessoas.json)
```

---

## Requisitos

- Python 3.7+
- pandas==2.3.3
- numpy==2.3.4
- python-dateutil==2.9.0.post0
- pytz==2025.2

### Instalar dependências

```bash
# Criar um virtualenv (recomendado)
python3 -m venv .venv

# Ativar o virtualenv
source .venv/bin/activate  # Linux/Mac
# ou
.\.venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

---

## Como Usar

### 1. Clonar o repositório
```bash
git clone https://github.com/emerson16inacio/modulo-ia-aws-clound.git
cd modulo-ia-aws-clound
```

### 2. Configurar ambiente
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Executar um exercício
```bash
python3 "Atividade1/exercicio1.py"
```

### 4. Sair do virtualenv
```bash
deactivate
```

---

## Estrutura do Projeto

```
modulo-ia-aws-clound/
├── Atividade1/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade2/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade3/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade4/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade5/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade6/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── Atividade7/
│   ├── exercicio1.py
│   ├── exercicio2.py
│   ├── exercicio3.py
│   └── exercicio4.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Notas Importantes

- **APIs Externas:** Os exercícios de Atividade 6 requerem conexão com a internet.
- **Pandas:** O exercício 1 de Atividade 7 requer a biblioteca pandas instalada.
- **Virtualenv:** É recomendado usar um virtualenv para isolar as dependências do projeto.
- **Encoding:** Todos os arquivos usam UTF-8 como encoding padrão.

---

## Autor

Criado como parte do módulo "IA AWS Cloud" - Escola da Nuvem

**Data:** Novembro de 2025

---

## Licença

Este projeto é fornecido como material educacional.
