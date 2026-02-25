class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l,r = 0 , len(height)-1
        max_area = 0
        
        while l<r:

            if height[l] < height[r]:

                area = height[l] * (r-l)

                l = l+1
            else:

                area = height[r] * (r-l)

                r = r-1
            
            max_area = max(area , max_area)

        return max_area

        