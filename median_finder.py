import heapq

class Solution:
    def lastStoneWeight(self, stones):

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0
if __name__ == "__main__":
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    result = s.lastStoneWeight(stones)
    print("Final Stone Weight:", result)