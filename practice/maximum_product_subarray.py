class Solution:
    def maxProduct(self, nums):
        max_prod = min_prod = ans = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if x < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(x, max_prod*x)
            min_prod = min(x, min_prod*x)
            ans = max(ans, max_prod)
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))