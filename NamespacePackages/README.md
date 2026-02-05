# Estudo: Namespace Packages (PEP 420)

Este repositório serve para demonstrar e validar o comportamento dos **Implicit Namespace Packages** no Python.

## O que estou a testar

**Ausência de ```__init__.py```**: Confirmar que o Python trata pastas normais como pacotes se estiverem no path.

**Fusão de Namespaces**: Como o Python combina duas pastas físicas diferentes sob o mesmo nome de importação (noinit).#