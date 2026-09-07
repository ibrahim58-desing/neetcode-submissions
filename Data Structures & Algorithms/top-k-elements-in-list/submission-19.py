class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rep={ }
        tup=[]

        for i in range(len(nums)):
            if nums[i] in rep:
                rep[nums[i]]+=1
            else:
                rep[nums[i]]=1    

        for key,value in rep.items():
            tup.append((key,value))


        tup.sort(key=lambda x:x[1] , reverse=True)  

        result=[] 

        for i in range(k):
            result.append(tup[i][0])

        return result    
