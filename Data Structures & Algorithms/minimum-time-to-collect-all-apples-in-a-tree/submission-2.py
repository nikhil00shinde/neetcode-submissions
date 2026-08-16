class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node,p):
            ans = 0

            for v in adj[node]:
                if v != p:
                    temp = dfs(v,node)
                    if temp > 0 or hasApple[v]:
                        ans += 2 + temp
            return ans

        return dfs(0,-1)

        