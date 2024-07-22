class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        
        max = len(candyType)//2
        
        count = set(candyType)
        

        if max < len(count):
            return max
        else:
            return len(count)
