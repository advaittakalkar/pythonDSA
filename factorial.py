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
    for i in range(2, n+1):  # runs from 2 to n    tc = n
        result = result * i
    return result


#drivers code
n = int(input("Enter the number"))
a=fact(n)
print(a)


