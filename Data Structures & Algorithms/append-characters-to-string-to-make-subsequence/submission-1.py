class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        n = len(t)
        for ch in s:
            if j < n and t[j] == ch:
                j+=1
        
        return n - j