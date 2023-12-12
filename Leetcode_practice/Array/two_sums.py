class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in prevMap:
               return [i, prevMap[diff]]
            prevMap[nums[i]] = i
        