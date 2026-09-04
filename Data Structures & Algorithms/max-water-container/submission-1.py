class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0,n-1
        ans = 0
        while l < r:
            lv = heights[l]
            rv = heights[r]
            ans = max(ans, min(lv,rv)*(r-l))
            if lv > rv:
                r-=1
            else:
                l+=1
        
        return ans

        