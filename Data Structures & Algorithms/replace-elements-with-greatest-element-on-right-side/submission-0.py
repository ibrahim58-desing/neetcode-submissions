class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            high=-1
            for j in range(i+1,len(arr)):
               
                if arr[j]>high:
                    high=arr[j]

            arr[i]=high
        return arr