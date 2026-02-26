class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        occured = {}
        
        if len(s) != len(t):
            return False
        
        
        for i in range(len(s)):
            
            if s[i] in occured:

                occured[s[i]] = occured[s[i]]+1
            else:
                occured[s[i]] = 1
            
            
            if t[i] in occured:

                occured[t[i]] = occured[t[i]] -1
            else:

                occured[t[i]] = -1
        
        if any(element != 0 for element in occured.values()):
            return False
        else:
            return True



