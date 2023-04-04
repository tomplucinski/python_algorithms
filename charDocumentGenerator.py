def generateDocument(characters, document):
    unicodeMap = {}
    for letter in document:
        encodedLetter = ord(letter)
        if encodedLetter not in unicodeMap:
            unicodeMap[encodedLetter] = 1
        else:
            unicodeMap[encodedLetter] += 1

    for char in characters:
        encodedChar = ord(char)
        if encodedChar in unicodeMap:
            unicodeMap[encodedChar] -= 1

    for x in unicodeMap:
        if unicodeMap[x] > 0:
            return False

    return True
