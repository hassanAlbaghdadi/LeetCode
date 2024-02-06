class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        for c in t:
            if c not in hm:
                return False
            else:
                hm[c] -= 1
        for i in hm:
            if hm[i] != 0:
                return False
        print(hm)
        return True

