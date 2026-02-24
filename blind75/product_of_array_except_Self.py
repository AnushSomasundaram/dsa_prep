# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
#         prefix = []
#         postfix = []
#         output = []
#         i = 0
#         j = len(nums)-1
#         present_postfix = 1
#         present_prefix = 1
#         while i < len(nums):
            
#             present_prefix = present_prefix * nums[i]
#             present_postfix = present_postfix * nums[j]
#             postfix.insert(0,present_postfix)
#             prefix.append(present_prefix)
#             j = j-1
#             i = i+1
        
#         temp = 0
#         while temp<len(nums):

#             if temp == 0 :

#                 output.append(postfix[temp+1])
            
#             elif temp == len(nums)-1:

#                 output.append(prefix[temp-1])

#             else:

#                 output.append(postfix[temp+1]*prefix[temp-1])
            



#             temp = temp+1

#         print(prefix,postfix)
#         return output
                


class Solution(object):
    def productExceptSelf(self, nums):


        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):

            output[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range (len(nums)-1, -1, -1):
            
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        
        return output