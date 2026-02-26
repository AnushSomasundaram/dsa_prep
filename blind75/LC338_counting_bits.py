class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # res =[]
        # for i in range(0,n+1):
        #     j =i
        #     count =0
            
        #     while j>0:
        #         count += j%2
        #         j = j >> 1
            
        #     res.append(count)
        
        # return res


        # dynamic programming

        dp =[0] * (n+1)

        offset = 1

        for i in range(1,n+1):

            if offset * 2 == i:

                offset = i
            
            dp[i] = 1 + dp[i-offset]
        
        return dp