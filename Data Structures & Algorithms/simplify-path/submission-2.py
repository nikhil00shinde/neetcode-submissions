class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        n = len(path)
        i = 0
        while i < n:
            j = i
            if path[j] == '/':
                while j < n and path[j] == '/':
                    j += 1
            else:
                s = ""
                while j < n and path[j] != '/':
                    s += path[j]
                    j += 1
                if s == ".." and st:
                    st.pop()
                elif s != "." and s != "..":
                    st.append(s)
                
                # print(s,st)
            i = j
        ans = ""
        n = len(st)
        if n == 0:
            return "/"
        for i in range(n):
            ans += "/"+st[i]
        return ans

            
            


        