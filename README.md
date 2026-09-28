# Urna Eletrônica

Simulação de urna eletrônica em Python, com votação, validação de arquivos e apuração de votos (eleições presidencial e municipal).

## Como funciona

O sistema é dividido em três etapas, executadas nesta ordem:

| Etapa | Arquivo | Função |
|-------|---------|--------|
| 1. Votação | `Urn.py` | Registra os votos e gera arquivos criptografados na pasta `file/` |
| 2. Validação | `Validation.py` | Confere a autenticidade do arquivo e libera a apuração |
| 3. Apuração | `Descryptography.py` | Descriptografa e conta os votos |

Há também o `Debuger.py`, usado para testes da função de hash.

## Requisitos

- Python 3

## Como executar

Na pasta do projeto:

```bash
python Urn.py
python Validation.py
python Descryptography.py
```

### 1. Urn.py (votação)

1. Digite a **chave de comunicação** (1 a 5 caracteres; você escolhe e deve lembrar depois).
2. Digite a **validação do arquivo**: `82731642`
3. Escolha o tipo de eleição:
   - `[1]` Presidencial — Deputado Federal, Deputado Estadual, Senador, Governador e Presidente
   - `[2]` Municipal — Vereador e Prefeito
4. Digite o número de cada candidato e confirme o voto.
5. Ao finalizar, os votos são salvos criptografados em `file/`.

### 2. Validation.py (validação)

1. Informe o nome do arquivo gerado (ex.: `82731642736`).
2. Se o arquivo for válido, digite a senha: `encryption72#`
3. Em caso de erro (arquivo inválido ou senha errada após 3 tentativas), os arquivos em `file/` são removidos.

### 3. Descryptography.py (apuração)

1. Digite a **mesma chave de comunicação** usada na urna.
2. O programa lê o arquivo validado, descriptografa e exibe a contagem dos votos.

## Credenciais de demonstração

| Uso | Valor |
|-----|--------|
| Validação do arquivo (`Urn.py`) | `82731642` |
| Nome do arquivo esperado | `82731642736` |
| Senha de segurança (`Validation.py`) | `encryption72#` |
| Chave de comunicação | Escolhida pelo usuário (mesma em `Urn.py` e `Descryptography.py`) |

## Estrutura do projeto

```
├── Urn.py                 # Urna / votação
├── Validation.py          # Validação dos arquivos
├── Descryptography.py     # Apuração
├── Debuger.py             # Testes de hash
├── file/                  # Arquivos de voto gerados
└── README.md
```

## Observação

Este é um projeto acadêmico/demonstrativo. A criptografia usada é didática e não deve ser aplicada em sistemas reais de votação.
