class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {i :[] for i in range(n)}

        heap = [(0,src,0)]

        best ={(src,0):0}

        for f,d,p in flights:
            adj[f].append((d,p))

        while heap:
            cost,node,fligt_used = heapq.heappop(heap)

            if cost > best[(node, fligt_used)]:
                continue


            if node == dst:
                return cost

            if fligt_used == k +1:
                continue

            for d , p in adj[node]:
                new_cost = cost+p
                new_flight = fligt_used+1

                if new_cost < best.get((d, new_flight), float("inf")):
                    best[(d, new_flight)] = new_cost
                    heapq.heappush(heap, (new_cost, d, new_flight))

        return -1


        