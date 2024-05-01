"""def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


#drivers code
n = int(input("Enter the number"))
print(fact(n))"""


def fact(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result


#drivers code
n = int(input("Enter the number"))
a=fact(n)
print(a)
