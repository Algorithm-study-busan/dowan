import bisect

#수정본1
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n-2):
            for j in range(i+1, n-1):

                k = bisect.bisect_left(nums, nums[i] + nums[j], j+1)
                count += k - j - 1
        
        return count