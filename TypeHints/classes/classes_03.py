from classes_01 import Animal
from classes_02 import get_animal_name

from utils import cyan_print, sep_print


class Dog(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name!r} faz au au")

    def run(self) -> None:
        cyan_print(f"{self.name!r} está correndo...")


class Cat(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name!r} faz miau")


if __name__ == "__main__":
    # Type Checkers
    dog = Dog("Dog")  # dog É UM Animal
    cat = Cat("Cat")  # cat É UM Animal

    sep_print()

    get_animal_name(dog)
    get_animal_name(cat)

    dog.make_sound()
    cat.make_sound()

    sep_print()

    dog2: Animal
    dog2 = Dog("Dog2")
    dog2.run()

    sep_print()
