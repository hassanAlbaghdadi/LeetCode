import heapq;
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = []
        for n in set(nums):
            heapq.heappush(result, n)
            if len(result)>3:
                heapq.heappop(result)
        if len(result) == 3:
            return result[-3]
        return result[-1]


        