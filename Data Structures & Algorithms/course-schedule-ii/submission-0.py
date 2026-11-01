class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            adj[a].append(b)

        visting = set()
        complted = set()
        order = []

        def dfs(curr):

            if curr in visting:
                return False

            if curr in complted:
                return True

            visting.add(curr)

            for neg in adj[curr]:
                if not dfs(neg):
                    return False

            visting.remove(curr)
            complted.add(curr)
            order.append(curr)

            return True

        for cous in range(numCourses):
            if not dfs(cous):
                return []
        return order



        