class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = set()
        for n in nums:
            if n in hm:
                return True
            hm.add(n)
        return False