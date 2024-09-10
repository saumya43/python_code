#Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive
from operator import length_hint


def min_length_subarray(nums, target):
    l, total = 0, 0
    length = float("inf")

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            length = min(length, r-l+1)
            total -= nums[l]
            l += 1
    return 0 if length == float("inf") else length

print(min_length_subarray([2,3,1,2,4,3], 6))