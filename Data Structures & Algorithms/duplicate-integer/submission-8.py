class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp: set = set()
        return any([1 if n in temp else temp.add(n) for n in nums])