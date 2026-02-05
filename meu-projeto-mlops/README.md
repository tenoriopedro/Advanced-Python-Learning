# UV Workspace: Integração de Apps e Libs

Este repositório é a resolução prática de um desafio de arquitetura Python utilizando **UV Workspaces**. O objetivo foi criar um ambiente de desenvolvimento monorepo onde aplicações e bibliotecas coexistem e se comunicam sem passos de _build_ intermediários.

## 🎯 O Desafio (Critérios de Sucesso)

O ambiente foi configurado para garantir três comportamentos específicos:

1. **Execução Direta**: Capacidade de correr `uv run api` sem erros de importação.

2. **Visibilidade de Pacotes**: A `api` consegue importar módulos da `lib` (`from meu.common.logger import log`).

3. **Hot-Reloading (Editable Mode)**: Alterações no código da `libs/common` refletem-se imediatamente na `api` sem necessidade de reinstalação (`pip install`) ou reconstrução de _wheels_.

## 🏗 Arquitetura da Solução

1. **Workspace Unificado**

O `pyproject.toml` na raiz define o workspace, englobando `apps/*` e `libs/*`. Isto cria um único `uv.lock` e um único ambiente virtual (`.venv`) partilhado por todos os membros.


2. **Resolução de Dependências (Workspace Sources)**

A gestão de dependências internas evita caminhos relativos rígidos (`../../`) dentro da lista principal de dependências. Em vez disso, utiliza-se a funcionalidade de **Sources** do UV.

No `pyproject.toml` da API, a dependência é declarada pelo nome abstrato:

```TOML

dependencies = ["meu-common"]
```

E a resolução é redirecionada para o workspace local através da tabela de configuração:
```TOML

[tool.uv.sources]
meu-common = { workspace = true }
```

**O que isto garante:**

- **Abstração**: O código pede "meu-common", não importando se vem do disco ou da cloud.

- **Editable by Default:** Ao usar `workspace = true`, o UV sincroniza o pacote em modo editável, garantindo que alterações na pasta `libs/common` sejam refletidas instantaneamente na `api` (Hot-Reloading).