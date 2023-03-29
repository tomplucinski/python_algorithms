def shiftCharacters(string, key):
    result = ''
    letters = list('abcdefghijklmnopqrstuvwxyz')

    for char in string:
        idx = letters.index(char)
        key %= len(letters)
        idx += key
        if idx > len(letters) - 1:
            idx -= len(letters)
        result += letters[idx]
    return result
