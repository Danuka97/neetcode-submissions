class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            adj[a].append(b)

        visted = set()
        complted = set()

        def dfs(curr):

            if curr in visted:
                return False

            if curr in complted:
                return True
            
            visted.add(curr)

            for neg in adj[curr]:
                if not dfs(neg):
                    return False

            visted.remove(curr)
            complted.add(curr)
            return True
        
        for cous in range(numCourses):
            if not dfs(cous):
                return False
        return True


