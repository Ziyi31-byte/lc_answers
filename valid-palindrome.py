# 66ms, beats 25%, O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_i, right_i = 0, len(s)-1
        while left_i < right_i:
            while not s[left_i].isalnum(): 
                left_i += 1
                if left_i>right_i:
                    return True
            left = s[left_i].lower()

            while not s[right_i].isalnum(): 
                right_i -= 1
                if right_i<left_i:
                    return True
            right = s[right_i].lower()

            if left != right: 
                return False
            else:
                left_i+= 1
                right_i-=1
        return True
# 59ms, beats 40%, weird as this is O(2n) while the above should be O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return True if s==s[::-1] else False
# space O(1), optimized from first sol
class Solution:
	def isPalindrome(self, s: str) -> bool:
		i, j = 0, len(s) - 1
		while i < j:
			a, b = s[i].lower(), s[j].lower()
			if a.isalnum() and b.isalnum():
				if a != b: return False
				else:
					i, j = i + 1, j - 1
					continue
			i, j = i + (not a.isalnum()), j - (not b.isalnum())
		return True
