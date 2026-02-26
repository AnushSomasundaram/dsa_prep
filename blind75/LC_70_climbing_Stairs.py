class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dynamic programming break it down into a tree

        # we're using memoization
        # bottom up dynmic programming approach

        one = 1
        two = 1

        for i in range(n-1):

            temp = one

            one = one + two

            two = temp 
            
        return one 









