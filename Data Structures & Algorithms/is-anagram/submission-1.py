class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_text = "".join(sorted(s))
        sorted_text_1 = "".join(sorted(t))

        if sorted_text == sorted_text_1:
            return True
        else:
            return False    

     