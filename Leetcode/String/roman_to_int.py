def romanToInt(s):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    for i in range(0, len(s)):
        if s[i] == 'I' and i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
            value = value - dict[s[i]]
        elif s[i] == 'X' and i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
            value = value - dict[s[i]]
        elif s[i] == 'C' and i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M'):
            value = value - dict[s[i]]
        else:
            value = value + dict[s[i]]

    return value


if __name__ == "__main__":
    s = "MCMXCIV"
    print(romanToInt(s))
