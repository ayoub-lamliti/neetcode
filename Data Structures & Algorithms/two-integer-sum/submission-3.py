class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_left = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numbers_left:
                return [numbers_left[diff], i]
            numbers_left[num] = i
        return []