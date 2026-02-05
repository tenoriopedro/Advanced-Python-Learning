# 🛠️ Guia de Configuração e Ambiente

Este documento detalha o fluxo de trabalho utilizando o **uv** — um gestor de pacotes extremamente rápido escrito em Rust — e as normas de configuração de **Git** e **Variáveis de Ambiente**.

---

## 📦 Gerenciamento com `uv`

O `uv` substitui ferramentas como `pip`, `poetry` e `pyenv` com performance superior.

### 1. Instalação do `uv`

**Windows (PowerShell):**
```powershell
iwr [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) -useb | iex
```
**Linux / macOS (curl):**
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

### 2. Inicialização do Projeto

Se iniciares um projeto do zero:

```Bash
uv init nome-do-projeto
```

Ou dentro de um projeto existente:

```Bash
uv init
```

### 3. Gestão de Dependências e Ambiente

O uv cria o ambiente virtual (venv) e instala tudo automaticamente:

- Sincronizar ambiente: `uv sync`

- Adicionar pacotes: `uv add requests ruff pyright`

- Remover pacotes: `uv remove requests`

- Importar de requirements.txt: `uv add -r requirements.txt`

### 4. Execução

Executa scripts sem necessidade de ativar o ambiente manualmente:

```Bash
uv run src/main.py
```

## ⚙️ Configuração do Git

Padronização de ambiente para evitar conflitos de "fim de linha" (Line Endings) entre Windows e Linux.

**Configuração Global**

```Bash

# Identificação
git config --global user.name "O Teu Nome"
git config --global user.email "teu@email.com"

# Padronização de Branch e Finais de Linha
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global core.eol lf
```

**Fluxo de Trabalho (Workflow)**
```Bash

# Primeiro Commit
git add .
git commit -m "initial"
git remote add origin URL_REPO_SSH
git push origin main -u

# Commits seguintes
git add .
git commit -m "MENSAGEM"
git push
```

# 🔑 Variáveis de Ambiente (.env)

O projeto utiliza o `python-dotenv` para gerir credenciais e configurações sensíveis.

**Configuração:**

1. Localiza o ficheiro `.env-example.`

2. Cria uma cópia e renomeia para `.env.`

3.  Preenche as variáveis conforme necessário.

**Teste de Validação:** Ao correr o projeto, o sistema verificará a configuração:

- `✅ Check dotenv: dotenv is working fine`   Configuração correta.

- `❌ Check dotenv: Not working. Read the README.md`  O ficheiro `.env` não foi encontrado ou está mal configurado.