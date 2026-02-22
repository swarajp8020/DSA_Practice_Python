class Solution:
    def climbingStairs(self, n):
        if n<=2:
            return n
        
        a,b = 1, 2
        for _ in range(3, n + 1):
            a, b = a + b
        return b
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbingStairs(2))