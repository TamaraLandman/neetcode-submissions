class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_word = sorted(s)
            word = "".join(sorted_word)
            d[word].append(s)
        ans = []
        for key in d:
            ans.append(d[key])

        return ans