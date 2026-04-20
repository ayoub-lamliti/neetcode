class Solution:
    def search(self, nums: List[int], target: int) -> int:
        find = [n for n in nums if n == target]
        if find:
            return nums.index(target)
        return -1