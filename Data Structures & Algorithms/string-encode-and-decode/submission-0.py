class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
        while pos < len(s):
            j = pos
            while s[j] != "#":
                j += 1
            length = int(s[pos:j])
            res.append(s[j+1:length+j+1])
            pos = j+1+length
        return res


