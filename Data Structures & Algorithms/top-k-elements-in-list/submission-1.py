class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        sd = dict(sorted(hm.items(), key=lambda item: item[1],reverse=True))
        ans = []
        i = 0
        for key,val in sd.items():
            if i < k:
                ans.append(key)
            i+=1
        return ans
        

