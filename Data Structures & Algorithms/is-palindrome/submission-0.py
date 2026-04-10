class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

 
        s = s.casefold()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        links = 0
        rechts = len(s) -1

        while links < rechts:
            if s[links] == s[rechts]:
                links +=1
                rechts -= 1
            else:
                return False
 
                
        return True
                



            

        
        