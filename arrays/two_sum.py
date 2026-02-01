from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i
        return[]
if __name__ == "__main__":
    solver = Solution()
    my_nums = [2, 7, 11, 15]
    my_target = 9
    result = solver.twoSum(my_nums, my_target)
    print(f"Input: nums={my_nums}, target={my_target}")
    print(f"Output: {result}")