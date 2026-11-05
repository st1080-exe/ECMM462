# ECMM462 Continuous Assessment
# Question 1 part 1 and 2 code
# Takes a text and applies the ceasar shift and then block transposition
# Takes a cipher text and reverts block transposition and ceasar shift

# base test variables
s = 5
p = [3,1,6,2,5,4]

text = "SECURITY"

# block filler letter
fillerLetter = "X"

# ceasar shift code
# shifts every letter in the given text down the alphabet by the given shift amount
def ceasarShift(input, shift):

    # alphabet referrence
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    result = ""

    for i in range(len(input)):

        # finds letter in alphabet
        num = alphabet.index(input[i])

        # shifts it down
        if(num + shift) <= 24:
            result += alphabet[num + shift]

        # if out of bounds, returns to start and continues count
        else:
            num = (num + shift) - 26
            result += alphabet[num]

    return result

# block transposition code
# jumbles up order of letters based on given permutation
# if theres an uneven number of letters then it fills the space with filler letters
def blockTransposition(input, permutation):

    result = ""

    # gets length of permutation block and text
    blockLen = len(permutation)
    textLen = len(input)

    # if there is an uneven amount it adds filler
    if textLen % blockLen != 0:
        for i in range (blockLen - (textLen % blockLen)):
            input += fillerLetter

    # shuffles around letters
    for i in range(int(len(input)/blockLen)):
        for j in range(blockLen):
            result += input[permutation[j]-1 + (blockLen*i)]

    return result

# undoes block transposition code
# returns letters to intended order based on given permutation
# attempts to remove any filler letters originally added
def blockDeposition(input, permutation):

    tempWord = []
    result = ""

    blockLen = len(permutation)
    textLen = len(input)

    # if the input isnt valid, return an error
    if(textLen%blockLen != 0):
        return("text length error")

    # fill up a placeholder word
    for i in range(textLen):
        tempWord.append(fillerLetter)

    # place the letters in the placeholder word based on the permutation order
    for i in range(int(textLen/blockLen)):
        for j in range(blockLen):
            letter = input[j + (blockLen*i)]
            tempWord[permutation[j]-1 + (blockLen*i)] = letter

    # remove any filler letters off the end
    while True:
        i = 1
        if(tempWord[-1] == fillerLetter):
            del tempWord[-i]
            i += 1
        else:
            break

    # rearrange everything back into a string
    for i in range(len(tempWord)):
        result += tempWord[i]

    return result

# encrypts a text by ceasar shift and then block transposition
def e(shift, permutation, plaintext):
    cipherText =  ceasarShift(blockTransposition(plaintext, permutation),shift)
    print(cipherText)
    return cipherText

# encrypts a text by undoing the block transposition and then ceasar shift
# the ceasar shift decription doesnt require a seperate un-doing function since the algorithm works with a negative shift as well
def d(shift, permutation, ciphertext):
    plaintext = blockDeposition(ceasarShift(ciphertext, -shift), permutation)
    print(plaintext)
    return plaintext