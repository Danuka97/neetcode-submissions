from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies (same as before)
        counts = Counter(nums)
        
        # 2. Create buckets where the INDEX is the frequency
        # We need len(nums) + 1 buckets (to account for 0 frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Populate the buckets
        for num, freq in counts.items():
            buckets[freq].append(num)
            
        # 3. Read the buckets backwards (from highest frequency to lowest)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        