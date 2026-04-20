class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums: dict = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
        dict_nums = sorted(dict_nums.items(), key=lambda item: item[1], reverse=True)
        _list = []
        while k:
            _list.append(dict_nums[k-1][0])
            k -= 1
        return _list