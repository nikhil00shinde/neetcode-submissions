class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        ans = 0
        for ch in s:
            if ch == '(':
                op += 1
            else:
                op -= 1
            if op < 0:
                ans += abs(op)
                op = 0
        
        return  ans + op
