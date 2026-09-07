class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for char in s:
            if char=="(":
                ans.append(")")
            elif char=="{":
                ans.append("}")
            elif char=="[":
                ans.append("]")
            elif not ans or ans.pop()!=char:
                return False
        return not ans        

                
        