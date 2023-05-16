# 110ms, beats 55%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        values = sorted(list(d.items()), key = lambda x: x[1])
        res = []
        for i in range(1,k+1):
            res.append(values[-i][0])
        return res
