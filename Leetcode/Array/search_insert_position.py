def searchInsertPosition(nums, target):
    for i in range(0, len(nums)):
        if nums[i] >= target:
            print(i)
            break
    print(i+1)


if __name__ == "__main__":
    nums = [1, 3, 5, 7]    # sorted array given
    target = 8
    searchInsertPosition(nums, target)