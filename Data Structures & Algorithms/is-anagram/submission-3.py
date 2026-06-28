class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}
        for char in s:
            sHash[char] = 1 + sHash.get(char, 0)
        for char in t:
            tHash[char] = 1 + tHash.get(char, 0)

        return sHash == tHash
        
        