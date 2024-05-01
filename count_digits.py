n = int(input("enter the number"))
count =0
while n>0:
    count = count+1
    n=int(n/10)    # or n//10 will also do --> gives floor
print(count)

