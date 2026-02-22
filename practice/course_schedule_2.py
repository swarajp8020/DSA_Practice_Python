from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) == numCourses:
            return result
        else:
            return []
if __name__ == "__main__":

    sol = Solution()

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    print("Course Order:", sol.findOrder(numCourses, prerequisites))
