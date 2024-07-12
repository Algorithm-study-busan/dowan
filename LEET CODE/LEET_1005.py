class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:

        nums.sort()
        count = 0

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                count += 1
                if count == k:
                    break        
       

        if (k-count)%2 != 0:
            nums.sort()
            nums[0] = -nums[0]
        
        return sum(nums)
        