def find_maximum(nums):
    if not nums:
        return None
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


if __name__ == "__main__":
    nums = [12,2,232, 2333]
    print(find_maximum(nums))