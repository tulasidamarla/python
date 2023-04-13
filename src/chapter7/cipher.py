##
# This program encrypts a file using the Caesar cipher.
# For ex the below command encrypts the file input.txt and places the result into encrypt.txt
# python cipher.py input.txt encrypt.txt
# The below command decrypts(-d) the file encrypt.txt and places the result into output.txt.
# python cipher.py -d encrypt.txt output.txt
#

from sys import argv

DEFAULT_KEY = 3


def main():
    key = DEFAULT_KEY
    inFile = ""
    outFile = ""
    files = 0  # Number of command line arguments that are files.

    for i in range(1, len(argv)):
        arg = argv[i]
        if arg[0] == "-":
            # It is a command line option.
            option = arg[1]
            if option == "d":
                key = -key
            else:
                usage()
                return

        else:
            # It is a file name.
            print("its a file name")
            files = files + 1
            if files == 1:
                inFile = arg
            elif files == 2:
                outFile = arg

    # There must be two files
    if files < 2:
        print("files", files)
        usage()
        return

    # Open the files.
    inputFile = open(inFile, "r")
    outputFile = open(outFile, "w")

    # Read the characters from the file.
    for line in inputFile:
        for char in line:
            newChar = encrypt(char, key)
            outputFile.write(newChar)

    # Close the files.
    inputFile.close()
    outputFile.close()


## Encrypts upper- and lowercase characters by shifting them according to a key.
# @param ch the letter to be encrypted
# @param key the encryption key
# @return the encrypted letter
#
def encrypt(ch, key):
    LETTERS = 26  # Number of letters in the Roman alphabet.
    if "A" <= ch <= "Z":
        base = ord("A")
    elif "a" <= ch <= "z":
        base = ord("a")
    else:
        return ch  # Not a letter.
    offset = ord(ch) - base + key
    if offset > LETTERS:
        offset = offset - LETTERS
    elif offset < 0:
        offset = offset + LETTERS
    return chr(base + offset)


## Prints a message describing proper usage.
#
def usage():
    print("Usage: python cipher.py [-d] infile outfile")


# Start the program.
main()
