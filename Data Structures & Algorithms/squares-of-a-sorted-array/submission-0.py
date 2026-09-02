class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        A = []
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        j = i-1
        while j >= 0 and i < n:
            if abs(nums[j]) > abs(nums[i]):
                A.append(nums[i]*nums[i])
                i+=1
            else:
                A.append(nums[j]*nums[j])
                j-=1
        while j >= 0:
            A.append(nums[j]*nums[j])
            j-=1
        while i < n:
            A.append(nums[i]*nums[i])
            i+=1
        return A
