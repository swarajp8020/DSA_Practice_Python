class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest,  i + nums[i])
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))