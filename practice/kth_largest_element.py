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
    nums = [3,2,1,5,6,4]
    k = 2
    print("Arrays: ", nums)
    print("K = ", k)
    print("Kth Largest: ", sol.findKthLargest(nums, k))