def runLengthEncoding(string):
    result = []
    count = 1
    for i in range(1, len(string)):
        prevLetter = string[i - 1]
        currentLetter = string[i]
        if prevLetter != currentLetter or count == 9:
            result.append(str(count))
            result.append(prevLetter)
            count = 0

        count += 1

    result.append(str(count))
    result.append(string[len(string) - 1])
    return "".join(result)
