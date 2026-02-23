def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
if __name__ == "__main__":
    nums = [11,-2,2,7]
    target = 9
    print(two_sum(nums, target))