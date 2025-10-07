def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))