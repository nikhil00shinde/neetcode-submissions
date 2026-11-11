class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        one, zero = 0, 0
        i,j = 0, 0
        n = len(nums)
        cnt = 0
        while j < n:
            if nums[j]:
                one += 1
            else:
                zero += 1
            while i < j and zero > k:
                if nums[i]:
                    one -= 1
                else:
                    zero -= 1
                i += 1
            
            if k >= zero:
                cnt = max(cnt, j - i + 1)
            j += 1
        return cnt