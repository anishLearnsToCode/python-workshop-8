vowels = ('a', 'e', 'i', 'o', 'u')


def isVowel(character: str) -> bool:
    return character in vowels


print(''.join([character if isVowel(character) else '_' for character in 'without']))
