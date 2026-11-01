import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = {i : [] for i in range(1,n+1)}

        heap = [(0,k)]
        dist = {i:float("inf") for i in range(1,n+1)}
        dist[k] = 0

        for u,v,w in times:
            adj[u].append((v,w))

        while heap:
            cost,node = heapq.heappop(heap)

            if cost > dist[node]:
                continue

            for neg,wei in adj[node]:
                new_cost = cost+wei

                if new_cost < dist[neg]:
                    dist[neg] = new_cost

                    heapq.heappush(heap,(new_cost,neg))

            max_dist = max(dist.values())


        return max_dist if max_dist != float("inf") else -1
