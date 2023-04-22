def main():
    print(isPalindrome("A man, a plan, a canal—Panama!"))
    print(isPalindrome("Go hang a salami, I’m a lasagna hog"))
    print(isPalindrome("Madam, I’m Adam"))

    # Testing with a helper function
    text = "A man, a plan, a canal—Panama!"
    print(substringIsPalindrome(text, 0, len(text)-1))
    text = "Go hang a salami, I’m a lasagna hog"
    print(substringIsPalindrome(text, 0, len(text)-1))
    text = "Madam, I’m Adam"
    print(substringIsPalindrome(text, 0, len(text)-1))


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


def substringIsPalindrome(text, start, end):
    # Separate case for substrings of length 0 and 1.
    if start >= end:
        return True
    else:
        # Get first and last characters, converted to lowercase.
        first = text[start].lower()
        last = text[end].lower()
        if first.isalpha() and last.isalpha():
            if first == last:
                # Test substring that does’t contain the matching letters.
                return substringIsPalindrome(text, start + 1, end - 1)
            else:
                return False
        elif not last.isalpha():
            # Test substring that does’t contain the last character.
            return substringIsPalindrome(text, start, end - 1)
        else:
            # Test substring that does’t contain the first character.
            return substringIsPalindrome(text, start + 1, end)


# Invoke main method
main()
