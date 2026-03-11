# nums = [3,2,1,5,6,4]
# k = 2
# # Output: 5

import heapq


def kth_largest(nums: list, k: int) -> int: 

#use simple sorting algo 
#nums.sort()
#return nums[-k]

# but if they ask not to use sort method

#use heap, as heap will always have minimum value as parent, min heap

#the idea is have the size of heap equal k, 
#so when we add items to heap, if the size is greater than k then pop an item
# at the end return the 0th item as it will always have the smallest number

    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


nums = [3,2,1,5,6,4]
k = 2

print(kth_largest(nums, k))