class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        path = []
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
        backtrack(0, target)
        return result
if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8

    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:", sol.combinationSum2(candidates, target))