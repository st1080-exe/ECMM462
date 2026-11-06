# ECMM462 Continuous Assessment
# Question 1 part 3 code
# Takes a plain text, its corresponsing cipher text, and an unknown cipher text and figures out the ceasar shift and the block permutation
# It then returns these 2 values along with the plain text from the previously unknown cipher text

fillerLetter = "X"

# test variables
KNOWN_PLAINTEXT =  "KNOWNPLAINTEXTCANREVEALWEAKCIPHERS"
KNOWN_CIPHERTEXT = "YYAVHZELPWYTYECILNWGHPLPTLAPNVIPISDC"
CHALLENGE_CIPHERTEXT = "NEVLLEPLLDPCHTSDCPJYDPPVPCLLHPIIIVII"

# cesar shift code taken from layercipher.py
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

# gets shift based on given plain text and cipher text
def ceasarShiftDecode(plainText, cipherText, blockLen):

    shift = 0

    # grabs first portion of text based on given block length
    sampleC = (cipherText[:blockLen])
    sampleP = (plainText[:blockLen])

    #shifts section through alphabet until it matches the cipher text
    for i in range(26):

        testWord = sorted(ceasarShift(sampleP, i))
        testC = sorted(sampleC)

        #if samples match exactly after a shift return the shift number
        if testWord == testC:
            shift = i

    return shift

# gets the permutation based on the plain text and the ceasar shifted cipher text
def blockPermutation(plainText, partDecodedText, blockLen):

    # gets amount of blocks
    blockNum = int(len(partDecodedText)/blockLen)

    groupedC = []
    groupedP = []

    permutation = []

    # sorts both texts into their blocks
    for i in range(blockNum):

        groupedC.append(partDecodedText[(i*blockNum):(i*blockNum)+(blockLen)])
        groupedP.append(plainText[(i*blockNum):(i*blockNum)+(blockLen)])

    # goes through the blocks until it reaches the first one with no duplicate letters
    # duplicate letters cause errors in figuring out the permutation
    for i in range(blockNum):

        if(hasNoDuplicates(groupedC[i])):

            # searches for the letter and adds the found index to the permutation
            sampleC = groupedC[i]
            sampleP = (plainText[(i*blockNum):(i*blockNum)+(blockLen)])

            for j in range(blockLen):

                num = sampleP.index(sampleC[j])

                permutation.append(num+1)

            break

    return permutation

# returns true if a given list has no duplicates
def hasNoDuplicates(input):
    if len(input) != len(set(input)):
        return False
    return True

# un-does block transposition based on given permutation
# taken from layercipher.py
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

# releaves the shift, permutation, and plain text of the challenge cipher given the parameters
def revealChallengeText(plainText, cipherText, challengeText):

    # gets shift from known plain and cipher text
    shift = ceasarShiftDecode(plainText, cipherText, 6)

    # applies ceasar shift on known cipher text
    partiallyDecoded = (ceasarShift(cipherText, -shift))

    # gains permutation based on known cipher text
    permutation = blockPermutation(plainText, partiallyDecoded, 6)

    # applies decoding on the challenge text
    challengeTextReveal = (blockDeposition(ceasarShift(challengeText, -shift), permutation))

    # prints discovered key values and plain text
    print(f"Shift: {shift}")
    print(f"Permutation: {permutation}")
    print(f"Recovered plaintext: {challengeTextReveal}")

# main
def main():

    # gets user input
    knownPlainText = input().strip().upper()
    knownCipherText = input().strip().upper()
    challengeCipherText = input().strip().upper()

    # computes result based on input
    revealChallengeText(knownPlainText, knownCipherText, challengeCipherText)

main()