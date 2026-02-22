from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        components = 0

        def dfs(node):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components


if __name__ == "__main__":

    sol = Solution()

    n = 5
    edges = [[0,1],[1,2],[3,4]]

    print("Connected Components:",
          sol.countComponents(n, edges))