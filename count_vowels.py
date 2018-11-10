def vowel_count(txt):
    if not isinstance(txt, str):
        raise TypeError('invalid input')

    vowels = 'aeiou'
    newtxt = txt.lower()
    noduplicates = set(newtxt)
    duplication = len(newtxt)-len(noduplicates)
    vowelstring = ""

    for i in vowels:
        if i in noduplicates:
            vowelstring += str(i)

    return (vowelstring, duplication)


if __name__ == "__main__":      
    print(vowel_count('welcomea'))