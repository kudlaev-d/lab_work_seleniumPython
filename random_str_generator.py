from random import choice
from string import ascii_letters

def generate_random_string(length: int) -> str:
    """Метод генерации случайной строки заданной длины"""
    letters = ascii_letters + ' '
    rand_string: str = ''.join(choice(letters) for i in range(length))
    return rand_string
