class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#"+st
        
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        lst = []
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            
            ans = s[i:j]
            ln = int(ans)

            i = j + 1
            j = i + ln
            lst.append(s[i:j])
            i = j
        return lst
