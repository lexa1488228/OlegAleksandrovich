def remove_palindroms(spells):
    for i in spells:
        if i.lower().split() == i[::-1].lower().split():
            spells.remove(i)
    return spells
