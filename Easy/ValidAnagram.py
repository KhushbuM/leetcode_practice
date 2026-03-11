

def validAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    anagramMap = {}

    for i in s:
        anagramMap[i] = anagramMap.get(i, 0) + 1

    for j in t:
        if j not in anagramMap:
            return False
            
        anagramMap[j] = anagramMap[j] - 1

        if anagramMap[j] == 0:
            del anagramMap[j]       

    return not anagramMap


s = "anagram"
t = "nagaram"

print(validAnagram(s, t))

