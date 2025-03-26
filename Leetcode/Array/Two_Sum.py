# My solution - Bruteforce approach   O(n2) O(1)
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i in range(0, len(nums)):
#         for j in range(0, len(nums)):
#             if i == j:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 return (i, j)


# a little enhancement in bruteforce approach
# def twoSum(self, nums: List[int], target: int) -> List[int]:     #O(n2)  O(1)
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):                       # next loop from i+1
#             if i == j:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 return (i, j)

# Here we can make it O(n2) O(1)  --> O(n) O(n) - we give more imp to time than space,
# space can be increased but no compromise on time

# solution using hashMap

def twoSum(nums, target):
    hash_map = {}   # hashmap is implemented as dictionary in python
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in hash_map:
            print(i, hash_map[diff])
        else:
            hash_map[nums[i]] = i
    return


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target)
