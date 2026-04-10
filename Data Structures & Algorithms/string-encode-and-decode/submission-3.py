class Solution:

    def encode(self, strs: List[str]) -> str:
        erg = ""
        for i in strs:
            erg += "(;)"+i 
        
        return erg
        
    def decode(self, s: str) -> List[str]:
        
        erg = s.split("(;)")
        erg.pop(0)
        return erg
