class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(numbers: List[int], target: int) -> List[int]:
            l,r = 0, len(numbers)-1
            res = []
            visited = set()
            while l<r:
                # print(l,r) # test
                s = numbers[l]+numbers[r]
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    if numbers[l] not in visited and numbers[r] not in visited:
                        res.append([numbers[l],numbers[r]])
                        visited.add(numbers[l])
                        visited.add(numbers[r])
                    l+=1
                    r-=1
                
            return res

        visited = set()
        res = []
        numbers = collections.deque(nums)
        for i in nums:
            if i in visited: 
                numbers.popleft()
                continue
            target = 0-i
            numbers.popleft()
            pairs = twoSum(numbers,target)
            if pairs:
                for x in pairs:
                    res.append([i]+x)
            visited.add(i)
        
        return res
