class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ourput = False
        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            
            else:
                ourput = False
            my_set.add(i)
        return ourput

            
