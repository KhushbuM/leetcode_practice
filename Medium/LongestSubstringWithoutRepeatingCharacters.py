# Input: "abcabcbb"
# Output: 3
# "abc" is the longest substring without repeating characters

# Input: "bbbbb"
# Output: 1



def longest_unique_substring(s: str) -> int:
    subSet = set()
    l = 0
    res = 0
    # best_start = 0
    # best_len = 0
    
    for r in range(len(s)):
        while s[r] in subSet:
            subSet.remove(s[l])
            l += 1
        subSet.add(s[r])
        res = max(res, r - l + 1)

    #   if they ask to return substring
        # curr_len = right - left + 1
        # if curr_len > best_len:
        #     best_len = curr_len
        #     best_start = left

    #return s[best_start:best_start + best_len]

    return res    

       
s = "abcabcbb"
result = longest_unique_substring(s)
print("Result : ", result)           
