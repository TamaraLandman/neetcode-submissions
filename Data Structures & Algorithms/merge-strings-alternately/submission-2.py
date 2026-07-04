class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        ans = ""

        smallest = min(len(word1), len(word2))

        for i in range(smallest):
            ans += word1[l]
            ans += word2[r]
            l += 1 
            r += 1

        if len(word1) > smallest:
            ans += word1[smallest::]
        else:
            ans += word2[smallest::]
        return ans
            