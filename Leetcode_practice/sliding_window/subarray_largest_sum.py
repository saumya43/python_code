# Find a non empty subarray with the largest sum and return left and right index of the max subaary sum
class Solutions:
    def largestsum(self, nums):
        maxsum = nums[0]
        currsum = 0
        L = 0
        maxL, maxR = 0, 0
        for R  in range(len(nums)):
            if currsum < 0:
                currsum = 0
                L = R
            
            currsum = currsum + nums[R]
            if currsum > maxsum:
                maxsum = currsum
                maxL, maxR = L, R

        return [maxL, maxR]

    
