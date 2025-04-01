def validParenthesis(s):
    cnt1 = 0  # ()
    cnt2 = 0  # []
    cnt3 = 0  # {}
    for char in s:
        if char == "(":
            cnt1 = cnt1 + 1
        elif char == "[":
            cnt2 = cnt2 + 1
        elif char == "{":
            cnt3 = cnt3 + 1
        elif char == ")":
            cnt1 = cnt1 - 1
        elif char == "]":
            cnt2 = cnt2 - 1
        else:
            cnt3 = cnt3 - 1

    if cnt1 == 0 and cnt2 == 0 and cnt3 == 0:
        print("valid")
    else:
        print("not valid")


if __name__ == "__main__":
    s = '{({[]})}'
    validParenthesis(s)
