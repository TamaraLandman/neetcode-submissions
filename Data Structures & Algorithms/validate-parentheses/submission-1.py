class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"(" : ")", "{" : "}", "[" : "]"}
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if p != closeToOpen[char]:
                    return False


        if len(stack) != 0:
            return False
        return True