from classes_01 import Animal

from utils import cyan_print, sep_print


def get_animal_name(animal: Animal) -> None:
    cyan_print(f"'get_animal_name' | Classe: {type(animal).__name__}")
    cyan_print(f"'get_animal_name' | {animal.name = !r}")
    sep_print()


if __name__ == "__main__":
    # Type Checkers
    dog = Animal("Dog")  # dog É UM Animal
    cat = Animal("Cat")  # cat É UM Animal

    sep_print()

    get_animal_name(dog)
    get_animal_name(cat)
