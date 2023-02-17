"Authors: Aydan O'Brien and Nicholas Engle"
def rescramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = evenChars + oddChars
    return cipherText

def rescramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + oddChars[i]
        plainText = plainText + evenChars[i]

    if len(oddChars) > len(evenChars):
        plainText = plainText + oddChars[-1]

    return plainText