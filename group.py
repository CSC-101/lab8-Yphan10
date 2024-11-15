def groups_of_3(nums: list[int]) -> list[list[int]]:
    result = []
    for i in range(0, len(nums), 3):
        result.append(nums[i:i + 3])
    return result
