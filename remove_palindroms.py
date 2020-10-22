def remove_palindroms(spells):
    for j in spells:
        sl = j.upper()
        if sl == sl[::-1]:
            spells.remove(sl)
    return spells
