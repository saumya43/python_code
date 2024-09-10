def window_k(nums, k):
    window = set()
    l = 0
    for r in range(len(nums)):
        if r - l + 1 > k:
            window.remove(nums[l])
            l = l+ 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False

print (window_k([1, 2, 3, 2, 3, 3], 3))