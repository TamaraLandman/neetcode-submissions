class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        ans = []
        for word in strs:
            # create a sorted word that is not a list
            sortedWord = tuple((sorted(word)))
            if sortedWord in d:
                d[sortedWord] += [word]
            else:
                d[sortedWord] = [word]

        for key in d:
            ans.append(d[key])

        return ans
