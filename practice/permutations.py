class Solution:
    def permute(self, nums):
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return result
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print("Input", nums)
    print("Permutations:")
    for p in sol.permute(nums):
        print(p)