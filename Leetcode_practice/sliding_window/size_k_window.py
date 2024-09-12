#Given an array, return True if there are two elements within a window of size k that are equal
def window_k(nums, k):
    l = 0
    Map = set()
    for r in range(len(nums)):
        if r-l+1 > k:
            Map.remove(nums[l])
            l = l+1
        if nums[r] in Map:
            return True
        Map.add(nums[r])

    return False


print (window_k([1, 2, 3, 2, 3, 3], 3))