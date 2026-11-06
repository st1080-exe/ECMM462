# ECMM462 Continuous Assessment
# Question 2 part 3 code
# takes given hash values and obscures them without changing their value

# test variables
x1 = "10110110"
x2 = "00110101"
x3 = "11001010"

hashVals = [x1, x2, x3]

# taken from the myhash.py script
# rotates the left most value to the end of the list
def rotateToLeft(input):

    return input[1:] + input[0]

# taken from the myhash.py script
# adds 2 hash values together based on the x or function
def addHash(hash1, hash2):

    result = ""

    #if the 2 values are the same, add 0, if they differ, add 1
    for i in range(len(hash1)):
        if hash1[i] == hash2[i]:
            result += "0"
        else:
            result += "1"

    return result

# alters given hash values in ways that still retain their value
def collision(input):

    blockLen = len(input)

    # 3 buffers to account for an odd block length
    # when used they cancel out a buffer for odd hash blocks
    bufferA = "00000001"
    bufferB = rotateToLeft(bufferA)
    bufferC = addHash(bufferA, bufferB)

    # makes a lift of all the buffers to be used
    changes = [bufferA] * blockLen

    # if odd insert odd buffers
    if blockLen % 2 == 1:
        changes[-2] = bufferB
        changes[-1] = bufferC

    blocks = []

    for i in range(blockLen):

        # adds given blocks to obscuring buffers
        blocks.append(addHash(input[i], changes[i]))

    print("Colliding message:", " ".join(blocks))



# asks the user for hash values and prints the result
def main():

    amount = int(input("how many hash values do you want to enter? "))

    values = []

    for i in range(amount):
        hash = input(f"enter hash value number {i+1}: ")
        values.append(hash)

    collision(values)

main()
    