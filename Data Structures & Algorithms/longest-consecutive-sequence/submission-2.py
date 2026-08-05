class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ln = 0

        for num in st:
            if (num-1) not in st:
                tp = 1
                while (num + tp) in st:
                    tp += 1
                ln = max(ln,tp)
        return ln