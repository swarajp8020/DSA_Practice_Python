class Solution:
    def permutations(self, nums):
        nums.sort()
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
                if i>0 and nums[i] == nums[i - 1] and not used[i - 1]:
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
    nums = [1,1,2]
    print("Input:", nums)
    print("Unique Permutations:")
    for p in sol.permutations(nums):
        print(p)