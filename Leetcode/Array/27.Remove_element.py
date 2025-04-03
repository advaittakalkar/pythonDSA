# def removeElement(nums,val):  # Here I used the dictionary to remove the number and its count and print other numbers according to their count
#     hashmap = {}
#     mylist = []
#     for number in nums:
#         if number in hashmap:
#             hashmap[number] = hashmap[number] + 1
#         else:
#             hashmap[number] = 1
#
#     for i, cnt in hashmap.items():
#         while cnt!=0 and i!=val:
#             mylist.append(i)
#             cnt = cnt - 1
#     print(mylist)
def removeElement(nums,val):
    k = 0
    for number in nums:
        if number != val:
            nums[k] = number
            k = k + 1
    print(k)
    print(nums)          # taking all elements to prior
    for x in range(k, len(nums)):
        nums[x] = 0
    print(nums)          # making other elements zero


if __name__ == "__main__":
    nums = [1,2,2,3]
    val = 2
    removeElement(nums, val)