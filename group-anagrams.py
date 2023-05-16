# 106ms, beats 63%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            s = ''.join(sorted(st))
            dic[s].append(st)

        return dic.values()
