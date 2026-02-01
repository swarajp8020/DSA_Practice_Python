class Solution:
    def missing_numbers(self, nums):
        res = 0

        for i in range (len(nums) + 1):
            res ^= i
        for x in nums:
            res ^= x
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.missing_numbers([3,0,1]))