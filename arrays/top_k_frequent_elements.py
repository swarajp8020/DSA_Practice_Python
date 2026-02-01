from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)
        
        ans= []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,3], 2))
    print(sol.topKFrequent([1], 1))
