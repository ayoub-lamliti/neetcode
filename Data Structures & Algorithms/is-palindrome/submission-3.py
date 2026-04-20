class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for ss in s.lower():
            if ss.isalnum():
                text += ss
        return text == "".join(text[::-1])