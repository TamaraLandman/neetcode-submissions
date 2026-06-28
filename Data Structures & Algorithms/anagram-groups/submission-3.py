class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for word in strs:
            sortedWord = str(sorted(word))
            d[sortedWord] = [word] + d.get(sortedWord, [])

        for val in d.values():
            ans.append(val)

        return ans