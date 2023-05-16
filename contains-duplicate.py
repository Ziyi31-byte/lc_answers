# 515ms, beat 99%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums: 
            if i in s: return True
            else: s.add(i)
# 560ms, beat 48%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(s) < len(nums): return True
        else: return False
# 566ms, beat 32% 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False
