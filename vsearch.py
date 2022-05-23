def search4vowels(phrase:str)-> set:
    """Выводим гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
def search4letters(phrase:str, letters:str='aeiou') -> set:
    '''Возвращает множество букв из 'letters', найденных в указанной фразе.'''
    return set(letters).intersection(set(phrase))
    













#for letter in word:
    #if letter in vowels:
        #found.setdefault(letter,0)
        #found[letter]+=1
#for k,v in sorted(found.items()):
    #print(k,'was found', v, 'time(s).')
        

        
