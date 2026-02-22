class Solution:
    def combinationSum(self, candidates, target):

        result = []
        path = []

        def backtrack(start, remaining):

            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)

        return result


if __name__ == "__main__":

    sol = Solution()

    candidates = [2, 3, 6, 7]
    target = 7

    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:", sol.combinationSum(candidates, target))
