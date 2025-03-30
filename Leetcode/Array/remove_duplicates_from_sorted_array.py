def removeDuplicates(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    print(list(dict))


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    removeDuplicates(nums)