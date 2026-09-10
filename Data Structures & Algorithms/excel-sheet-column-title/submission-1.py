class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber%26
            q = columnNumber//26
            ch = chr(ord('A')+r)
            ans.append(ch)
            columnNumber = q
        ans = ans[::-1]
        return "".join(ans)