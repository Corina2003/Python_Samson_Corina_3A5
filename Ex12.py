#Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
def group_by_rhyme(words):
    rhyme_groups= {}
    for word in words:
        if len(word)>2:
            rhyme= word[-2:]
        else:
            rhyme= word
        if rhyme not in rhyme_groups:
            rhyme_groups[rhyme]=[]
        rhyme_groups[rhyme].append(word)
    return list(rhyme_groups.values())
result = group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte'])
print(result)

