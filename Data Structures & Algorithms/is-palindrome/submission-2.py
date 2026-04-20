class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for ss in s.lower():
            if ss.isalpha() or ss.isdigit():
                text += ss
        return text == "".join(text[::-1])