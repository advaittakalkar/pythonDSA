def isPalindrome(string):
    string = string.lower()
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start = start + 1
        end = end - 1
    return True


if __name__ == "__main__":
    # string = "A man, a plan, a canal: Panama"
    string = "abba"
    print(isPalindrome(string))
