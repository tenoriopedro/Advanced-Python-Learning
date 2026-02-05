# Tipos básicos (explícito e implícito)

from typing import Final

name: str = "Pedro Tenório"
x: int = 22
y: float = 23.33
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b"whatever"


# Constantes
# Essa constante não costuma ser reatribuída, então a tipagem é redundante.
# O próprio valor já deixa claro que é uma string.
CONSTANT = "valor constante"


# Coleções
numbers_list: list[int] = [1, 2, 3]
two_value_tuple: tuple[str, int] = ("Valor", 234)
several_tuple: tuple[str, ...] = "a", "b", "c", "..."
set_numbers: set[int] = {1, 2, 3, 4}
set_immutable: frozenset[int] = frozenset([2, 3, 4, 5])
dictionary: dict[str, str] = {"chave": "valor", "chave2": "valor2"}
numbers: range = range(10)

# Outros tipos
nothin: None = None  # Representa ausência de valor
anything: object = 123  # Pode ser qualquer objeto
type_a: type[str] = str  # Referência ao tipo 'str' em si (não uma string)

# Constantes novamente
CONSTANT_B: Final[list[str]] = ["a", "b"]
constant_c: Final[dict[str, int]] = {"numero": 123, "outro_numero": 432}
