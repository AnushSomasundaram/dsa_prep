class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        one_count = 0

        # while n>=1:

        #     if n%2 != 0:

        #         one_count += 1

        #     n = n//2
        
        # return one_count
        
        while n:

            one_count += n%2

            n = n>>1
        
        return one_count

