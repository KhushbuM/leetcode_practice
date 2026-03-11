# Input:
# ["eat","tea","tan","ate","nat","bat"]
# [
# ["eat","tea","ate"],
# ["tan","nat"],
# ["bat"]
# ]
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagramMap = defaultdict(list)

    for item in strs:
        sorted_item = sorted(item)
        sorted_str = "".join(sorted_item)
        if sorted_str in anagramMap:
            anagramMap[sorted_str].append(item)
        else:
            anagramMap[sorted_str] = [item]



    return list(anagramMap.values())  


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))

