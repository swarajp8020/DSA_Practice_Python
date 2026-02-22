import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        dist = {}
        while heap:
            time, node = heapq.heappop(heap)
            
            if node in dist:
                continue
            dist[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (time + weight, neighbor))
        if len(dist) != n:
            return -1
        return max(dist.values())
if __name__ == "__main__":
    sol = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print("Network Delay Time:", sol.networkDelayTime(times, n, k))