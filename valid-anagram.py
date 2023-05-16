# 36ms, beat 97%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If they are different, return false...
            if s.count(idx) != t.count(idx):
                return False
        return True 
# 64ms, beats 33%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_table = [0]*26
        for i in s:
            letters_table[ord(i)%97] += 1
        for i in t:
            letters_table[ord(i)%97] -= 1
        for i in letters_table:
            if i != 0: return False
        return True
# 61ms, beats 40%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
