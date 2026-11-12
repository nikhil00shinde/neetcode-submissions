class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r = 0
        total = 0
        cnt = 0
        n = len(nums)
        size = 0
        while r < n:
            print(l,r)
            if total + k >= nums[r] * size:
                size += 1
                total += nums[r]
                r += 1
            elif l < n:
                size -= 1
                total -= nums[l]
                l += 1
            cnt = max(cnt, size)
        return cnt
            