class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for _str in strs:
            temp_str = "".join(sorted(_str))
            if temp_str in groups:
                groups[temp_str].append(_str)
            else:
                groups[temp_str] = [_str]
        return sorted(groups.values(), key=lambda item: len(item))