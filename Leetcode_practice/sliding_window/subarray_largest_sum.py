# Find a non empty subarray with the largest sum and return left and right index of the max subaary sum

def largestsum(nums):
    maxL , maxR = 0, 0
    currsum = 0
    maxsum = 0
    l = 0
    for r in range(len(nums)):
        if currsum < 0:
            currsum = 0
            l = r
        currsum = currsum + nums[r]
        if currsum > maxsum:
            maxsum = currsum
            maxL, maxR = l, r
    return [maxL, maxR]

print(largestsum([4,-1,2,-7,3,4]))  
