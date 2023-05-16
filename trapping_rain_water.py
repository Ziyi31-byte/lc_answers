# O(n), beats 77% time
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1 or n == 2: return 0
        l,r = 0, n-1
        while r>0 and height[r-1]>height[r]:
            r-=1
            if r == 0: return 0
        hl, hr = height[l], height[r]

        trapped = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                while height[l]<hl:
                    trapped+=(hl-height[l])
                    l+=1
                hl = height[l]
            else:
                r -= 1
                while height[r]<hr:
                    trapped+=(hr-height[r])
                    r-=1
                hr = height[r]

        return trapped
