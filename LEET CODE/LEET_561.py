class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:

        nums.sort()
        
        count = 0

        for i in range(len(nums)):
            if i%2 ==0:
                count = count + nums[i]
        
        return count
