def countOccurances(s, sub):
    count = 0
    for char in s:
        if char == "l":
            count = count + 1
    return count

if __name__ == "__main__":
    s = "hello world"
    sub = "l"
    count = countOccurances(s, sub)
    print(count)