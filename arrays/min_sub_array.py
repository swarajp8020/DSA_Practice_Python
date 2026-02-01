class Solution:
    def minSubArray(self, target, nums):
        left = 0
        total = 0
        ans = float('inf')
        
        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArray(7,[2,3,1,2,4,3]))