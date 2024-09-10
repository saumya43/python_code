# Find the length of the longest subarray, with the same value in each position
def longest_subarray(nums):
    length = 0
    l = 0
    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r 
        length = max(length, r-l+1)
    return length

print (longest_subarray([4, 2, 2, 3, 3, 3]))