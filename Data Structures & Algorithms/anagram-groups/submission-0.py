class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_groupAnagrams = []
        temp_list: dict[str, list] = dict()
        for i, _str in enumerate(strs):
            _str = "".join(sorted(_str))
            if _str in temp_list:
                temp_list[_str].append(i)
            else:
                temp_list[_str] = [i]

        for _str, _list in temp_list.items():
            temp = []
            for i in _list:
                temp.append(strs[i])
            list_of_groupAnagrams.append(temp)
            
        return sorted(list_of_groupAnagrams, key=lambda item: len(item))