class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for i in s:
            if i.isalnum():
                word.append(i.lower())

        if word == list(reversed(word)): return True

        return False
        