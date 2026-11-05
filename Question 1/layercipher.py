s = 5
p = [3,1,6,2,5,4]

text = "SECURITY"

fillerLetter = "X"


def ceasarShift(input, shift):

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    result = ""

    for i in range(len(input)):

        num = alphabet.index(input[i])

        if(num + shift) <= 24:
            result += alphabet[num + shift]

        else:
            num = (num + shift) - 26
            result += alphabet[num]

    return result

def blockTransposition(input, permutation):

    result = ""

    blockLen = len(permutation)
    textLen = len(input)

    if textLen % blockLen != 0:
        for i in range (blockLen - (textLen % blockLen)):
            input += fillerLetter

    for i in range(int(len(input)/blockLen)):
        for j in range(blockLen):
            result += input[permutation[j]-1 + (blockLen*i)]

    print(result)

def blockDeposition(input, permutation):

    tempWord = []
    result = ""

    blockLen = len(permutation)
    textLen = len(input)

    if(textLen%blockLen != 0):
        return("text length error")

    for i in range(textLen):
        tempWord.append(fillerLetter)

    for i in range(int(textLen/blockLen)):
        for j in range(blockLen):
            letter = input[j + (blockLen*i)]
            tempWord[permutation[j]-1 + (blockLen*i)] = letter

    while True:
        i = 1
        if(tempWord[-1] == fillerLetter):
            del tempWord[-i]
            i += 1
        else:
            break

    for i in range(len(tempWord)):
        result += tempWord[i]

    return result



print(blockDeposition("HXNJWZXYXDXX", p))
print(ceasarShift("XJHZWNYD", -s))

def e(shift, permutation, plaintext):
    return (blockTransposition(ceasarShift(plaintext,shift),permutation))

def d(shift, permutation, ciphertext):
    return (ceasarShift(blockDeposition(ciphertext, permutation), -shift))
