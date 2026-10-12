class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum
        count = [0] * (len(words) + 1)
        ans = []
        prev = 0
        for i in range(len(words)):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                prev += 1
            count[i+1] = prev

        for q in queries:
            start = q[1]
            end = q[0]
            ans.append(count[start+1] - count[end])
        return ans
        