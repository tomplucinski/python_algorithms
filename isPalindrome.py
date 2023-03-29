def isPalindrome(string):
    firstIdx = 0
    lastIdx = len(string) - 1
    while firstIdx < lastIdx:
        if string[firstIdx] != string[lastIdx]:
            return False
        firstIdx += 1
        lastIdx -= 1
    return True
