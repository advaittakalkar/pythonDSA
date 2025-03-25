# approach1:
# numList = [1,4,3,0,4,5,0,3]
# create a temp list and if you see non zero element add it to temp list
# at the end, add all zeroes

# approach2:

# def zeroesToEnd(numList):
#     count = 0
#     for i in range(0,len(numList)):
#         if numList[i] != 0:
#             numList[count] = numList[i]
#             count += 1
#
#     while count < len(numList):
#         numList[count] = 0
#         count += 1
#
#     print(numList)
#
#
# if __name__ == "__main__":
#     numList = [1, 2, 0, 4, 3, 0, 5, 0]
#     zeroesToEnd(numList)



# approach3:

def zeroesToEnd(numList):
    count = 0
    for i in range(len(numList)):
        if numList[i] != 0:
            numList[i], numList[count] = numList[count], numList[i]
            count += 1
    return numList


if __name__ == "__main__":
    numList = [3, 5, 0, 0, 4]
    new_list = zeroesToEnd(numList)
    print(new_list)