class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {}

        for i,char in enumerate(s):
            last[char] = i

        results = []
        start = 0
        end = 0


        
        for i,char in enumerate(s):

            end = max(end,last[char])

            if i == end:
                results.append(i - start + 1)
                start = i +1
        
        return results

            

        