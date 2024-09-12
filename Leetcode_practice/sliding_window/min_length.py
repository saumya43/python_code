#Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive
def min_length_subarray(nums, k):
    length = float("inf")
    total = 0
    l = 0
    for r in range(len(nums)):
        total = total + nums[r]
        while total >= k:
            length = min(length, r-l+1)
            total = total - nums[l]
            l = l+1
    return length


print(min_length_subarray([2,3,1,2,4,3], 6))