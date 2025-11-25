def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    return min(nums), max(nums)


print(min_max([1.5, 2, 2.0, -3.1]))
