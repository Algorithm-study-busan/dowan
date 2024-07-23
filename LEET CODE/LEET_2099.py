class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:


        for i in range(len(nums)):
            if len(nums) > k:
                nums.remove(min(nums))
            else:
                break
         
        return nums
