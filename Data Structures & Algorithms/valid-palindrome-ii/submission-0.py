class Solution:
    def validPalindrome(self, s: str) -> bool:

        if str(reversed(s)) == s: return True

        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                skipL =  s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
        return True







        