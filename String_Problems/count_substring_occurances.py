# # using count method
# def countSubstringOcc(string, substring):
#     cnt = string.count(substring)
#     print(cnt)
#
#
# if __name__ == "__main__":
#     string = "abcaaaaabcddereiopabc"
#     substring = "abc"
#     countSubstringOcc(string, substring)

##########################################################################################
# using find keyword
# def countSubstringOcc(string, substring):
#     count = 0
#     start = 0  # start looking for substring from 0th index
#     while True:
#         index = string.find(substring, start)  # searches substring starting from index start, if found, returns index, if no, returns -1
#         if index == -1:
#             break
#         count = count + 1
#         start = index + 1
#     print(count)
#
#
# if __name__ == "__main__":
#     string = "abcaaaaabcddereiopabc"
#     substring = "abc"
#     countSubstringOcc(string, substring)

###########################################################################################
# incredible method of finding occurrences of substring using slicing
def countSubstringOcc(string, substring):
    len_sub = len(substring)
    count = 0
    for i in range(len(string)-len_sub+1):   # so that it doesnt get out of bound
        if string[i:i+len_sub] == substring:
            count = count + 1
    print(count)


if __name__ == "__main__":
    string = "abcaaaaabcddereiopabc"
    substring = "abc"
    countSubstringOcc(string, substring)
