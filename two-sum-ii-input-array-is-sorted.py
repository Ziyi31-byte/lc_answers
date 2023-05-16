# beats 22% time and 30% space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            # print(l,r) # test
            s = numbers[l]+numbers[r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                return [l+1,r+1]
