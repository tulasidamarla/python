def main():
    print(isPalindrome("A man, a plan, a canal—Panama!"))
    print(isPalindrome("Go hang a salami, I’m a lasagna hog"))
    print(isPalindrome("Madam, I’m Adam"))


def isPalindrome(text):
    length = len(text)
    if length <= 1:
        return True
    else:
        # Get first and last characters
        first = text[0].lower()
        last = text[length - 1].lower()
        if first.isalpha() and last.isalpha():
            if first == last:
                return isPalindrome(text[1:length - 1])
            else:
                return False
        elif not last.isalpha():
            return isPalindrome(text[:length - 1])
        elif not first.isalpha():
            return isPalindrome(text[1:])


# Invoke main method
main()
