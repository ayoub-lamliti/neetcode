class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums: dict = {}
        for num in set(nums):
            dict_nums[num] = nums.count(num)
        return [key for key, _ in sorted(
            dict_nums.items(), key=lambda item: item[1], reverse=True)][:k]