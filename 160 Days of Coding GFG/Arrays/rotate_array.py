# approach :- ex. [ 1,2,3,4,5,6,7 ] d=2 expected output [ 3,4,5,6,7,   1,2 ]
# rotate/reverse whole array -- [7,6,5,4,3,2,1]
# if d=2   - rotate last two and rest [ 3,4,5,6,7  1,2]


# approach2: using temp list
# copy the rest elements to new list
# and then copy the first d elements after that


def rotate_array(numList, d):
    print(numList[d:len(numList):1] + numList[0:d:1])  # [2,6,1] +  [0,1,1]    [a:b:c]  a inclusive, b exclusive, c steps


if __name__ == "__main__":
    numList = [1,2,3,4,5,6,7]
    d = 2
    rotate_array(numList, d)

