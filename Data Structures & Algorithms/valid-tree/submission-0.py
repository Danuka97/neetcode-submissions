class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i :[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visted = set()

        def dfs(curr,pere):

            if curr in visted:
                return False

            visted.add(curr)

            for neb in adj[curr]:

                if neb == pere:
                    continue
                if not dfs(neb,curr):
                    return False

            return True

        return dfs(0,-1) and len(visted)==n

            
