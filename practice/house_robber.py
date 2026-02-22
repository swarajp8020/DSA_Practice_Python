class Solution:
    def rob(self, nums):
        prev1,prev2 = 0, 0
        for x in nums:
            curr = max(prev1, prev2 + x)
            prev2 = prev1
            prev1 = curr
        return prev1
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2,7,9,3,1]))