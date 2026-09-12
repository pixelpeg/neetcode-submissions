class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): #O(nlogn)
            return True
        else:
            return False

        