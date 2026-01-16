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
    
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        """
        Use ord(char) to get the unicode ASCII of the character
        The key in the res dict is the frequency array of english letters.
        The value is the original str arrays that have the same letter frequency.
        time: O(m * n)
        space: O(1) + key: max all strs are diff O(26 * m) = O(m) + values: m strs store into map, n is the longest length of strs O(m * n)
        """
        res = defaultdict(list)
        for s in strs:
            frequency = [0] * 26
            for char in s:
                frequency[ord(char) - ord('a')] += 1
            res[tuple(frequency)].append(s)
        
        return list(res.values())
