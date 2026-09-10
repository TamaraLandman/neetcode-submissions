class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        length = len(needle)
        for i in range(len(haystack)):
            word = haystack[i:length+i]
            if word == needle:
                return i 
        return -1
        