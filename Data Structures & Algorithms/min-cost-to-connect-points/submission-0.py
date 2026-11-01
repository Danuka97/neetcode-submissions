import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        adj = {i : [] for i in range(n)}


        for i in range(n):
            x1,y1 = points[i]
            for j in range(1+i,n):
                x2,y2 = points[j]

                cost = abs(x1-x2) +abs(y1-y2)

                adj[i].append((cost,j))
                adj[j].append((cost,i))

        heap = [(0,0)]
        visited = set()
        total_cost = 0

        while heap:
           cost,node = heapq.heappop(heap)

           if node in visited:
            continue
           visited.add(node)
           total_cost += cost

           for edge_cost,neg in adj[node]:
            if neg not in visited:
                heapq.heappush(heap,(edge_cost,neg))

        return total_cost

