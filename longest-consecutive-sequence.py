# 491ms, beats 47%
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        source= set()
        d = dict()
        # print(s) # test
        for i in s:
            if i+1 in s:
                d[i] = i+1
                if i-1 not in s:
                    source.add(i)
        res = set()
        # print(source) # test
        # print(d) # test
        for key in source:
            consecutive_lst = set()
            consecutive_lst.add(key)
            while key in d:
                key = d[key]
                consecutive_lst.add(key)
            res.add(len(consecutive_lst))
        if res != set(): return max(res)
        elif res == set() and nums != []: return 1
        else: return 0
