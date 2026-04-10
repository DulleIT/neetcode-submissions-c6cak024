class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        erg = {}

        for i in nums:
            if i in erg:
                return True
            else:
                erg[i] = True
        return False