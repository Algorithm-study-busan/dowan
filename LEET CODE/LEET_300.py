class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:


        dp = [1] * len(nums) #가장 짧은 부분집합의 크기는 1
 
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: #nums[i]보다 큰 숫자가 들어간 부분집합은 고려하지 않는다.
                    dp[i] = max(dp[i], dp[j] + 1)

    
        return max(dp)