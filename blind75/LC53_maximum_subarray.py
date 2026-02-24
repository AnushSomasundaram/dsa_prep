class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray = nums[0]
        curr_sum =0
        for n in nums:
        
            if curr_sum<0:
                curr_sum =0
            curr_sum = n +curr_sum

            max_subarray = max(curr_sum,max_subarray)

        return max_subarray