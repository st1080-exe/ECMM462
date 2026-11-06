# ECMM462 Continuous Assessment
# Question 2 part 2 code
# Gets an input of hash values from the user and outputs the result of ROTL and XOR of the values

# test variables
x1 = "10110110"
x2 = "00110101"
x3 = "11001010"

hashVals = [x1, x2, x3]

# runs the hash function
def hashFunction(values):

    # sets starting hash
    startingHash = values[0]

    for i in range(len(values)-1):

        #rotates starting hash and then adds it to the next hash
        startingHash = rotateToLeft(startingHash)
        startingHash = addHash(startingHash, values[i+1])

    return startingHash

# rotates the left most value to the end of the list
def rotateToLeft(input):

    return input[1:] + input[0]

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

# asks the user for hash values and prints the result
def main():

    amount = int(input("how many hash values do you want to enter? "))

    values = []

    for i in range(amount):
        hash = input(f"enter hash value number {i+1}: ")
        values.append(hash)

    print(f"Resulting hash value: {hashFunction(values)}")

main()