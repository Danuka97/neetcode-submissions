class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visted = set()

        def dfs(curr):

            if curr in visted:
                return

            visted.add(curr)

            for ne in adj[curr]:
                dfs(ne)

        count = 0

        for node in range(n):
            if node not in visted:
                count += 1
                dfs(node)

        return count
            
            