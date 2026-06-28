class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for i in s:
            if i in "abcdefghijklmnopABCDEFGHIJKLMNOP1234567890":
                word.append(i.lower())

        print(word)
        print(list(reversed(word)))
        if word == list(reversed(word)): return True

        return False
        