class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        time: O(m * n), m is the lenth of list strs, n is the shortest length in strs
        space: O(1)
        """
        n = len(strs[0])

        for i in range(n):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        
        return strs[0]
    
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        # 1. choose first element prefix
        # 2. loop the strs list, compare the current str with the prefix
        # 3. update the new prefix
        # 4. after the loop, will get the longest common prefix
        prefix = strs[0]

        for s in strs[1:]:
            n = len(prefix)
            for i in range(n):
                if i == len(s) or s[i] != prefix[i]:
                    prefix = s[:i]
                    break
        
        return prefix