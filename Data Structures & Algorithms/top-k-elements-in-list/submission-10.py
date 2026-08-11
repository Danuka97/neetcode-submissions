class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        def counts(nums:List[int]):
            conuts ={}
            for i in nums:
                if i not in conuts:
                    conuts[i] = 1
                else:
                    conuts[i] += 1
            return conuts
        freq = counts(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, cnt in freq.items():
            buckets[cnt].append(num)
        results = []
        for bucket in reversed(buckets):
            if bucket:
                for num in bucket:
                    results.append(num)
                if len(results) == k:
                    return results