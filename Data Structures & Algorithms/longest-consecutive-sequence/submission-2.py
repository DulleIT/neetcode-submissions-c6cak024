class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        elements = set()
        counter_streak = 1
        counter = 1

        for i in nums:
            elements.add(i)

        erg = list(elements)
        erg.sort()

        for i in range(len(erg) - 1):
            if erg[i+1] - erg[i] == 1:
                counter_streak += 1
                counter = max(counter, counter_streak)
            else:
                counter = max(counter, counter_streak)
                counter_streak = 1
                
        
        
        return counter
        