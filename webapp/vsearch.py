def search4vowels(phrase: str) -> set:
    """Выводим гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    '''Возвращает множество букв из 'letters', найденных в указанной фразе.'''
    return set(letters).intersection(set(phrase))
