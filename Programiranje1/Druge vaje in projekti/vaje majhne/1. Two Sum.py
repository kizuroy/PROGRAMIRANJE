def twoSum(nums: list[int], target: int) -> list[int]:
    idxs =  dict()
    for idx, num in enumerate(nums):
        if (target - num) in idxs:
            return [idxs[target - num], idx]
        idxs[num] = idx
    return []
