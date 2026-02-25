class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # cant write the code below
        # try:
        #     index = nums.index(target)
        # except:
        #     return -1
        
        # return index

        left , right = 0, len(nums)-1

        

        while left<=right:
            
            mid = (left+right)//2

            if target == nums[mid]:
                return mid

            #left sorted protion

            if nums[left] <= nums[mid]:

                if target> nums[mid] or target<nums[left]:

                    left = mid+1
                else:
                    right = mid-1
                
                
            # right sorted portion
            else:
                if target < nums[mid] or target>nums[right]:

                    right = mid - 1
                else:
                    left = mid + 1
                

        
        return -1
                
                


            
                
            
        
            
            

            
            


            