class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        

        erg_list = list(freq.keys())

        erg_list.sort(key=lambda x: freq[x], reverse=True)

        erg = []

        for i in range(k):
            erg.append(erg_list[i])

        
        return erg



        