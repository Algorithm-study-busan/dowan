class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        g.sort()
        s.sort()
        count = 0
        
        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    count +=1
                    del s[j]
                    break

        return count