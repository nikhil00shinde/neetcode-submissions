class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        n = len(nums)
        for i in range(n):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
        return prev+1