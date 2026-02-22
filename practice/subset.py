class Solution:
    def subsets(self, nums):
        result = []
        subset = []
        def backtrack(start):
            result.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return result
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print("Input: ", nums)
    print("Subsets: ")
    for s in sol.subsets(nums):
        print(s)