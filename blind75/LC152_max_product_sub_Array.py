class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        max_product = 1
        min_product = 1


        for num in nums:
            
            if num == 0:
                max_product = 1
                min_product = 1
            
            temp = max_product
            max_product = max(max_product*num,min_product*num,num)
            min_product = min (temp*num,num,min_product*num)
            res = max(res, max_product)

        return res

        
