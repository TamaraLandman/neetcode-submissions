class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        r = 0
        ans = ""

        while l < len(word1) and r < len(word2):
           ans += word1[l]
           ans += word2[r]
           r += 1
           l += 1

        if l < len(word1) -1:
            ans += word1[l:]
        else:
            ans += word2[r:]

        return ans
        


            
        