class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x:x[1])
        prev_end = float('-inf')
        removals = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1
        return removals
if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))