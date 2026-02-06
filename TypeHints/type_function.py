from utils import cyan_print, sep_print

sep_print()


def remove_duplicates(items: list[str]) -> list[str]:
    # `dict.fromkeys` gera um dicionário a partir da lista.
    to_dict = dict.fromkeys(items)
    # `list` converte o dict em lista, remove as duplicatas e mantém a ordem.
    return list(to_dict)


# Será removido
list_with_duplicates = ["luiz", "a", "b", "a", "c", "a", "d", "luiz"]
unique_items = remove_duplicates(list_with_duplicates)
# Saída - ['luiz', 'a', 'b', 'c', 'd']
cyan_print(f"{unique_items = }")
sep_print()


def is_image_file(filename: str) -> bool:
    # Algumas extensões comuns de imagens
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    # Garante que o nome do arquivo está em letras minúsculas sempre
    name_lowercase = filename.lower()
    # Termina com alguma das extensions ou não?
    return name_lowercase.endswith(extensions)


# Uso
filename = "arquivo.exe"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "imagem.JPEG"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "foto.png"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "meme.gif"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
sep_print()
