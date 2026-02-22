import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        result = 0
        while k:
            val, row, col = heapq.heappop(heap)
            result = val
            if col + 1 < n:
                heapq.heappush(heap,
                               (matrix[row][col + 1], row, col + 1))
            k -= 1
        return result
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 4
    print("Matrix:")
    for row in matrix:
        print(row)
    print("\nK =", k)
    print("Kth Smallest Element:", sol.kthSmallest(matrix, k))    