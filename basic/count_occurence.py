def count_occurence(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

if __name__ == "__main__":
    nums = [1,2,3,2,2,5]
    print(count_occurence(nums, 2))