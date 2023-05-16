# 263ms, beats 14%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_prod = [nums[0]]
        right_prod = [nums[-1]]
        for i in range(1,l):
            left_prod.append(left_prod[i-1]*nums[i])
            right_prod.append(right_prod[i-1]*nums[-i-1])
        res = []
        for i in range(0,l):
            if i == 0: 
                res.append(right_prod[-2])
            elif i == l-1:
                res.append(left_prod[-2])
            else:
                res.append(left_prod[i-1]*right_prod[l-i-2])
        return res
