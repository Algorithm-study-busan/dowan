class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        tmp = 0
        idx = 0

        x = set(nums)
        list_x = list(x)

        for i in list_x:
            if tmp < nums.count(i):
                tmp = nums.count(i)
                idx = i
        
        return idx