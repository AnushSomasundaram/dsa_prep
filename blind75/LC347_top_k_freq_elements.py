class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        occurance = [[] for i in range(len(nums)+1)] 
        res = []
        for n in nums:

            if n in count.keys():
                count[n] = 1 + count[n] 
            else :
                count[n] = 1
        print(count)
        
        for n,c in count.items():

            occurance[c].append(n)
        
        print(occurance)
        for element in occurance[::-1]:

            if len(element)!=0 :

                res = res +element
            
            if len(res) >= k:

                return res[0:k]

            