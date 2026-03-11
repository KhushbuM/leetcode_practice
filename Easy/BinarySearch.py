# nums = [-1,0,3,5,9,12]
# target = 9

# # Output: 4

def binary_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1          


nums = [-1,0,3]
target = 9

print(binary_search(nums, target))

#here we are dividing each time so n/2, n/4
# so n / 2*k = 1
# k = log 2 (n)
# O(log n)

# [] target = 1
# [1] target = 1
# [0, 1] target = 3
