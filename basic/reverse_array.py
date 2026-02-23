def reverse_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(reverse_array(nums))