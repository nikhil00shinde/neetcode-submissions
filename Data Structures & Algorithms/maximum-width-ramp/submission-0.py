class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        for i, x in enumerate(nums):
            if not st or x < nums[st[-1]]:
                st.append(i)
        
        ans = 0
        for j in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]] <= nums[j]:
                ans = max(ans, j - st.pop())
        
        return ans
        

