def validParenthesis(s):  # O(n) and O(n)
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    brackets = ['(', '[', '{' ]
    for char in s:
        if char in brackets:    # if its opening bracket then append
            stack.append(char)
        elif stack and stack[-1] == bracket_map[char]:  # if some opening bracket present in stack and current close bracket's equivalent open bracket is on the top then pop
            stack.pop()
        else:
            return False

    if not stack:
        return True
    else:
        return False


if __name__ == "__main__":
    s = '['
    print(validParenthesis(s))
