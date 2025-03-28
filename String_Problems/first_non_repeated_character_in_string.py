def nonRepeatedChar(my_string):   #time complexity is O(n)
    dict = {}

    for  char in my_string:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    for char in my_string:
        if dict[char] == 1:
            return char


if __name__ == "__main__":
    my_string = "hello world"
    print(nonRepeatedChar(my_string))