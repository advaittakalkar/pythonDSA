# Naive approach - sort first then get 2nd element  -- O(n log n)
# Better approach - two iteration search      -- O(2*n) -> O(n)
# Expected approach - One iteration search     -- O(n)

def secondHighest(numbers):
    l = -1    #float("-inf")
    sl = -1   #float("-inf")

    for i in numbers:
        if i > l:
            sl = l
            l = i

        elif i > sl and i < l:
            sl = i

    return sl


numList = [10,10,10]
secondLargest = secondHighest(numList)
print(f"second largest is {secondLargest}")

