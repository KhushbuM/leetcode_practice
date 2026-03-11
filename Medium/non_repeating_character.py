# Input:  "aabccdeff"
# Output: "b"
# input : "abccd"
# output: "d"

def non_repeating(s :str):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1


    for char in s:
        if freq[char] == 1:
            return char


    return "_"


s = "aaaaaa"
result = non_repeating(s)

print("RESULT : " + result)

