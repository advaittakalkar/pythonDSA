def countCharactersInString(string):    # time complexity - O(n) and space complexity - O(n)
    string = string.lower()
    dict = {}

    for char in string:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    print(dict)


if __name__ == "__main__":
    string = "Advait Takalkar"
    countCharactersInString(string)