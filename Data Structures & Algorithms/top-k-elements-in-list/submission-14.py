class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums: dict = Counter(nums)
        dict_nums = sorted(dict_nums.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in dict_nums[:k]]