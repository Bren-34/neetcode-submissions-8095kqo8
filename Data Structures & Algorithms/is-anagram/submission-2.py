class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(list(s))
        tlist = sorted(list(t))
        if slist == tlist:
            return True
        else:
            return False