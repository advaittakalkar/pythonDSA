def longestCommonPrefix(strs):
    res = ""
    prefix = strs[0]
    for i in range(1, len(strs)):  # 1,2
        while prefix != strs[i][:len(prefix)]:
            prefix = prefix[:-1]  # not inclusive of last character
            if not prefix:
                return ""
    print(prefix)


if __name__ == "__main__":
    strs = ["flow","flight","flower"]
    longestCommonPrefix(strs)
