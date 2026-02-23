class Solution:
    def minCostConnectionPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        edges.sort()
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            if rank[rootY] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        total_cost = 0
        edges_used = 0
        for cost, u, v in edges:
            if union(u,v):
                total_cost += cost
                edges_used += 1
                if edges_used == n -1:
                    break
        return total_cost
            
if __name__ == "__main__":

    sol = Solution()

    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

    print("Minimum Cost:",
          sol.minCostConnectionPoints(points))
            