# Input:
# ["eat","tea","tan","ate","nat","bat"]
# [
# ["eat","tea","ate"],
# ["tan","nat"],
# ["bat"]
# ]
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagramMap = defaultdict(list) #O(1)

    for item in strs: #O(n)
        sorted_item = sorted(item)  # O(n log n)
        sorted_str = "".join(sorted_item) 
        if sorted_str in anagramMap:
            anagramMap[sorted_str].append(item)
        else:
            anagramMap[sorted_str] = [item]

    return list(anagramMap.values())  


# total time complexity will be O(n * k log k), because for each word the sorting will be done for each character,
# so if characters are 3 then O (3 log 3) for all the words, so O(6 * 3 log 3)



strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))

