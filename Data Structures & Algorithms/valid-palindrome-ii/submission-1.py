class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        def isP(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        i = 0
        j = n - 1

        while i < j:
            if s[i] != s[j]:
                return isP(i+1,j) or isP(i,j-1)
            i += 1
            j -= 1
        return True