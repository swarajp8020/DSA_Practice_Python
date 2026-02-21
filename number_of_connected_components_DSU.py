class Solution:
    def countComponents(self, n, edges):

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True

        components = n

        for u, v in edges:
            if union(u, v):
                components -= 1

        return components


if __name__ == "__main__":

    sol = Solution()

    n = 5
    edges = [[0,1],[1,2],[3,4]]

    print("Connected Components (Union Find):",
          sol.countComponents(n, edges))