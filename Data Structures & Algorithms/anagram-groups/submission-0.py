from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            char_count = tuple(sorted(Counter(word).items()))
            anagrams[char_count].append(word)

        return list(anagrams.values())

      

