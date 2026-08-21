class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)
        if m > n: return False
        i = 0
        j = 0
        while j < m and i < n:
            if abbr[j].isdigit():
                num = 0
                while j < m and abbr[j].isdigit():
                    if num == 0 and int(abbr[j]) == 0:
                        return False
                    num = num * 10 + int(abbr[j])
                    j+=1
                
                if i + num <= n:
                    i += num
                else:
                    return False
            elif word[i] == abbr[j]:
                i+=1
                j+=1
            else:
                return False
            print(i,j)
            # j+=1
        return i >= n and j >= m

            