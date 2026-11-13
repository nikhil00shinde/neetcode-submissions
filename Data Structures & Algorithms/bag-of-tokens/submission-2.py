class Solution:
    def bagOfTokensScore(self, T: List[int], P: int) -> int:
        n = len(T)
        T.sort()
        cnt = 0
        ans = 0
        i,j = 0,n-1
        while i <= j:
            if T[i] <= P:
                P -= T[i]
                i += 1
                cnt += 1
            elif cnt > 0:
                P += T[j]
                j -= 1
                cnt -= 1
            else:
                break
            ans = max(cnt, ans)
        return ans
