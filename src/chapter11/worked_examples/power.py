def main():
    result = power(2, 11)
    print("pow:", result)
    print("Expected: 2048")

    result = efficientPower(2, 13)
    print("pow:", result)
    print("Expected: 8192")


## Computes lucky if a number contains digit 8.
# @param number
# @return boolean
def power(number, exponent):
    if exponent == 1:
        return number
    return number * power(number, exponent - 1)


def efficientPower(number, exponent):
    if exponent < 0:
        number = -number
        exponent = 1 / exponent;

    if exponent == 1:
        return number
    if exponent % 2 == 0:
        return efficientPower(number * number, exponent >> 1)
    else:
        return number * efficientPower(number * number, exponent >> 1)


# main method
main()
