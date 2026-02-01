
class Solution:
    def containsDuplicate(self,nums):
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,2,3,1]))
