from utils import cyan_print, sep_print


class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def make_sound(self) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    dog = Animal("Dog")
    cat = Animal("Cat")

    sep_print()

    cyan_print(f"{dog.name = !r}")
    cyan_print(f"{cat.name = !r}")

    sep_print()
