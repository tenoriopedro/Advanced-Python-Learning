# Python Advanced Workspace: Monorepo & Namespacing

Este repositório serve como um laboratório prático para a implementação de arquiteturas modernas de projetos Python. O foco principal é a gestão de múltiplos pacotes dentro de um único ecossistema (**Monorepo**) utilizando as funcionalidades avançadas do UV.
🛠 Arquitetura Técnica

## A estrutura utiliza três pilares fundamentais do Python moderno:

### 1. UV Workspaces

Em vez de gerir ambientes virtuais isolados para cada pasta, o projeto utiliza
o **UV Workspaces**. Isto permite que todos os pacotes partilhem o mesmo ficheiro
de bloqueio (```uv.lock```), garantindo consistência total de versões e 
facilitando o desenvolvimento local de pacotes interdependentes.

### 2. Native Namespace Packages

Todos os pacotes estão sob o namespace ```titan```. Isto significa que, embora estejam em pastas diferentes (```package_a```, ```package_b```), eles são importados como submodulos de uma raiz comum:

- ```from titan import mod_a```

- ```from titan import mod_b```

- ```from titan import mod_titan```

Esta abordagem elimina a necessidade de ficheiros ```__init__.py``` na raiz do namespace e permite a distribuição modular de código.

### 3. Type Stubs (```.pyi```)

O uso da pasta ```stubs/``` demonstra a separação entre a implementação e a definição de tipos. Isto é essencial para:

- Melhorar a experiência de desenvolvimento (IDE Autocomplete).

- Garantir a verificação estática de tipos (Mypy/Pyright) em módulos complexos ou dinâmicos.