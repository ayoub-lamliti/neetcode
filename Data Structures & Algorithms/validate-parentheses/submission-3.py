class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for ss in s:
            if ss in valid:
                stack.append(ss)
            elif not stack or ss != valid.get(stack.pop()):
                return False
        return not stack 
            