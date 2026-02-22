
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))