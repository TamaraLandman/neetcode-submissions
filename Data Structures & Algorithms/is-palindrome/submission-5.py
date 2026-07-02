class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        s = s.upper()
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        while l < r:
            if s[l] not in chars:
                l += 1
            elif s[r] not in chars:
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        return True
        