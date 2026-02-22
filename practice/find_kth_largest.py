import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([8,5,7,2,9,3], 3))