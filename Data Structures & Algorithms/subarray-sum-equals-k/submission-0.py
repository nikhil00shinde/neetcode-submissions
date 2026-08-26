class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        sm = 0
        ans = 0
        for num in nums:
            sm += num
            ans += hm[sm-k]
            hm[sm] += 1
        return ans