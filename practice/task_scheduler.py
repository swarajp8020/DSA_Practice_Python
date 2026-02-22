import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap:
            temp = []
            cycle = n + 1
            while cycle > 0 and maxHeap:
                curr = -heapq.heappop(maxHeap)
                if curr - 1:
                    temp.append(curr - 1)
                time += 1
                cycle -= 1
            for t in temp:
                heapq.heappush(maxHeap, -t)
            if not maxHeap:
                break
            time += cycle
        return time
if __name__ == "__main__":
    sol = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(sol.leastInterval(tasks, n))