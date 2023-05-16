# 81ms, beats 47%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
# 104ms, beats 43%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)): 
            num_j = target - sorted_nums[i]
            left, right = i+1, len(sorted_nums)-1
            mid = (left+right)//2
            while left <= right:
                if sorted_nums[mid] == num_j:
                    if sorted_nums[i] == sorted_nums[mid]:
                        return [i for i,n in enumerate(nums) if n == sorted_nums[mid]]
                    else:
                        return [nums.index(sorted_nums[i]),nums.index(sorted_nums[mid])]
                elif sorted_nums[mid] < num_j:
                    left = mid+1
                else:
                    right = mid-1
                mid = (left+right)//2
