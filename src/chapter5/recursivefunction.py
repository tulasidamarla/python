##
# This program demonstrates how to print a triangle using recursion.
#
def main():
    printTriangle(4)
    printTriangleReverse(0, 5)


## Prints a triangle with a given side length.
# @param sideLength an integer indicating the length of the bottom row
#
def printTriangle(sideLength):
    if sideLength < 1:
        return
    printTriangle(sideLength - 1)
    # Print the row at the bottom.
    print("[]" * sideLength)


def printTriangleReverse(start, end):
    if start == end:
        return
    printTriangleReverse(start + 1, end)
    # Print the row at the bottom.
    print("[]" * start)


# Start the program.
main()
