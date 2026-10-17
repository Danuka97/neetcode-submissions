class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for a in nums:
            data[a] = data.get(a,0) +1
        
        #{1:1,2:2,3:3}

        freq = [[]for _ in range(len(nums)+1)]

        for key,v in data.items():
            freq[v].append(key)
        #[[],[1],[2],[3],[],[]]

        res = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)

            if len(res) == k:
                return res


