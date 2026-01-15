from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        time: O(m * nlogn), m is the length of the list strs, n is the longest length of str in the list strs
        space: O(m * n)
        """
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        
        return list(res.values())