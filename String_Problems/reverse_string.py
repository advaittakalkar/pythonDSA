def reverse_string(s):  # time complexity - O(n)
    return s[::-1]


if __name__ == "__main__":
    s = "advait"
    string = reverse_string(s)
    print(f"string is {string}")
