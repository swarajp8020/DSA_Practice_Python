import heapq

class Solution:
    def kClosest(self, points, k):

        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for (dist, point) in heap]
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([(1,3), (-2,2), (5,8), (0,1)], 2))