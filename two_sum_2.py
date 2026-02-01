class Solution:
    def twoSum2(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s==target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum2([2,7,11,15], 9))