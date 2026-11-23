class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        nm = []
        i = 0
        n = len(s)
        p = 0
        sof = ""
        while i < n:
            ch = s[i]
            if ch.isalpha():
                # print(ch)
                sof += ch
            elif ch == ']':
                temp = sof
                sof = st.pop()
                count = nm.pop()
                sof += temp * count
            elif ch == '[':
                st.append(sof)
                nm.append(p)
                p = 0
                sof = ""
            else:
                p = p*10 + ord(ch) - ord('0')
               
            i += 1
        
        return sof
                

        