def generateDocument(characters, document):
    unicodeMap = {}
    for char in characters:
        if char not in unicodeMap:
            unicodeMap[char] = 0
        unicodeMap[char] += 1
    for letter in document:
        if letter not in unicodeMap or unicodeMap[letter] == 0:
            return False
        unicodeMap[letter] -= 1
    return True
