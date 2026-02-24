class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # count = []
        # for i in range(len(nums)):

        #     fixed = nums[i]
        #     test = i+1
            
        #     for test in range(test,len(nums)):

        #         if fixed + nums[test] == target:
        #             count = count + [i,test]

        #         test = test +1
            
        #     i = i+1
        
        # return count

        occured = {}
        sets = []
        for i in range(len(nums)):

            element = nums[i]
            required_number = target - element
            
            if required_number in occured:
                    sets = sets + [occured[required_number],i]
            
            
            if element not in occured:
                occured[element] = i
            
           

            
            #print(occured)            
        return sets
       
        

        
