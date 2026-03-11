# nums = [1,1,1,2,2,3]
# k = 2

# Output: [1,2]

def top_k_frequent(nums: list, k: int) -> list:
    freq = {}

    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    items = list(freq.items())

    items.sort(reverse=True, key = lambda x:x[1])   
    result = []
    for i in range(k):
        result.append(items[i][0])

    return result    

nums = [1,1,1,2,2,3]
k = 3
print(top_k_frequent(nums, k))

