class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_string = list(s)
        for c in t:
            if c in s:
                if c in list_string:
                    list_string.remove(c)
            else:
                return False
        if list_string:
            return False
        return True