class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        cur = ""
        for c in path + "/":
            if c == '/':
                if cur == '..':
                    if st:
                        st.pop()
                elif cur != "" and cur != ".":
                    st.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(st) 


            
            


        