class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        data = {}

        for a in nums:
            data[a] = data.get(a,0) +1
        
        freq = [[]  for _ in range(len(nums)+1)]

        for nums,count in data.items():
            freq[count].append(nums)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)

            if len(res)==k:
                return res
            
        

        