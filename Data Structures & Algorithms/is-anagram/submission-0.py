class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ergT = []
        ergS = []
        for i in s:
            ergS.append(i)
        
        for i in t:
            ergT.append(i)
        
        ergT.sort()
        ergS.sort()

        if ergS == ergT:
            return True

        return False
            


        
     