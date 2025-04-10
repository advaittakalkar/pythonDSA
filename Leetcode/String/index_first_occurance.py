# def indexFirstOccurance(haystack, needle):
#     index = haystack.find(needle)
#     print(index)

def indexFirstOccurance(haystack, needle):
    n = len(haystack)
    m = len(needle)
    for i in range(0, n-m+1):
        if haystack[i:i+m] == needle:
            print(f"first occurances is at index {i}")
            break


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    indexFirstOccurance(haystack, needle)