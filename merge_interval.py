class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x :x[0])
        res = []

        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))