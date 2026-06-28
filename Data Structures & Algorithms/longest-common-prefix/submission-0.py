class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        pref = ""
        i = 0

        while i < len(strs[0]):
            if strs[0][i] == strs[len(strs)-1][i]:
                pref += strs[0][i]
            else:
                break
            i += 1
        return pref


        
            
        