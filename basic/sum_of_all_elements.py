def array_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

if __name__ == "__main__":
    nums = [10, 20, 30]
    print(array_sum(nums))