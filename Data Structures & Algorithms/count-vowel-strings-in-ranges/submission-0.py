class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            count = 0
            word_list = words[q[0]: q[1]+1]
            for word in word_list:
                if word[0] in "aeiou" and word[-1] in "aeiou":
                    count += 1
            ans.append(count)
        return ans
        