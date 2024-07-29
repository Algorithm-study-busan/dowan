import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if len(nums) == 0:
            return [-1,-1]

        left = bisect.bisect_left(nums,target)
        right = bisect.bisect_right(nums,target) - 1

        if left == right+1:
            return [-1,-1]

        else:
            arr = [left, right]
            return arr
