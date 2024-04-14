# 4 задача
def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
