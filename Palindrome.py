def ispal(n):
    a = n
    rev = 0
    while n>0:
        r = n % 10
        rev = rev*10 + r
        n = n // 10
    return rev == a

#drivers code
n = int(input("Enter a number"))
if ispal(n):
    print("palindrome")
else:
    print("not palindrome")