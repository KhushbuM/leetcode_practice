#nums = [100, 4, 200, 1, 3, 2]
# Output: 4#

def longest_consecutive(nums: list) -> int:
    subSet = set(nums)
    longest = 0

    for num in subSet:

        if num - 1 not in subSet:
            current_num = num
            curr_len = 1

            while current_num + 1 in subSet:
                curr_len += 1
                current_num += 1

            longest = max(longest, curr_len)  

    return longest          

nums = [100, 4, 5, 1, 3, 2, 101, 102, 103,104]
print(longest_consecutive(nums))