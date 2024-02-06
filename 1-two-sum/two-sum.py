class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,n in enumerate(nums):
            find = target - n
            if find in hm:
                return [hm[find],i]
            hm[n] = i
        return

