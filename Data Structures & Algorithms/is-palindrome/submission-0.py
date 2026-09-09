class Solution:
    def isPalindrome(self, s: str) -> bool:
       arr = [char.lower() for char in s if char.isalnum()]
       i=0
       j=len(arr)-1
       while i<j:
        if arr[i]!=arr[j]:
            return False
        else:
            i+=1
            j-=1

     
       return True   
           