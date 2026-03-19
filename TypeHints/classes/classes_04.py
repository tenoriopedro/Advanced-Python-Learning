from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, Self, final, override

from utils import cyan_print, sep_print


class BaseAddress(ABC):
    def __init__(self, street: str, number: int) -> None:
        self.street: str = street
        self.number: int = number

    @abstractmethod
    def get_full_address(self) -> str: ...

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__

        attrs_list = [f"{k}={v!r}" for k, v in vars(self).items()]
        attrs_string = ", ".join(attrs_list)
        return f"{cls_name}({attrs_string})"


class NewAddress(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


class Address(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


@final
class CachedAddress(Address):
    _cache: ClassVar[dict[str, Self]] = {}

    def __new__(cls, street: str, number: int) -> Self:
        fake_id = f"{street}{number}".lower().replace(" ", "")

        if fake_id in cls._cache:
            cyan_print(f"JÁ CRIADO: {fake_id}")
            return cls._cache[fake_id]

        instance = super().__new__(cls)
        cls._cache[fake_id] = instance

        return instance

    def __init__(self, street: str, number: int) -> None:

        if not hasattr(self, "_initialized"):
            super().__init__(street, number)
            cyan_print(f"INICIALIZADO: {self}")
            self._initialized = True


type Addresses = dict[int, Address]


@dataclass
class Person:
    name: str
    age: int
    _addresses: Addresses = field(
        default_factory=dict[int, Address],
        init=False,
        repr=False,
    )
    _new_address_index = 0

    def add_address(self, *addresses: Address) -> None:

        for address in addresses:
            self._addresses[self._new_address_index] = address
            self._new_address_index += 1

    def get_address(self, index: int) -> Address | None:
        return self._addresses.get(index, None)


if __name__ == "__main__":
    sep_print()

    p1 = Person("Pedro", 25)
    a1 = Address("Address 1", 1)
    c1 = CachedAddress("Cached 1", 1)
    c2 = CachedAddress("Cached 2", 2)
    c3 = CachedAddress("Cached 3", 3)
    c31 = CachedAddress("Cached 3", 3)

    p1.add_address(a1, c1, c2, c3)

    cyan_print(p1)
    cyan_print(p1.get_address(0))
    cyan_print(p1.get_address(1))
    cyan_print(p1.get_address(2))

    sep_print()
