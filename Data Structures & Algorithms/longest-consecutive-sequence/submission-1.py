class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        vis = set()
        st = set()
        for num in nums:
            st.add(num)
        oans = 0
        for num in nums:
            ans = 0
            cur = num
            while num in st and num not in vis:
                vis.add(num)
                num += 1
                ans += 1
            hm[cur] = max(ans+hm[num],hm[cur])
            oans = max(hm[cur],oans)
        return oans
        
        