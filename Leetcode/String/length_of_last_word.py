def lastWordLength(s):
    list = s.split(" ")

    i = len(list)
    while i>=0:
        if len(list[i-1])>0:
            print(len(list[i-1]))
            break
        else:
            i = i-1


if __name__ == "__main__":
    s = "Hello World advaitta  "
    lastWordLength(s)