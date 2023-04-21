def main():
    lucky = isLucky(10)
    print("Lucky:", lucky)
    print("Expected: False")


## Computes lucky if a number contains digit 8.
# @param number
# @return boolean
def isLucky(number):
    if number < 10:
        if number == 8:
            return True
        else:
            return False
    lastDigit = number % 10
    if lastDigit == 8:
        return True
    else:
        return isLucky(number // 10)


# main method
main()
