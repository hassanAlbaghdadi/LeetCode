import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = []
        for n in set(nums):
            heapq.heappush(result, n)
            if len(result) > 3:
                heapq.heappop(result)
        if len(result) == 3:
            return result[-3]
        return result[-1]

            


# nums = list(set(nums))
#         nums.sort()
#         if len(nums) < 3:
#             return nums[-1]
#         return nums[-3]        