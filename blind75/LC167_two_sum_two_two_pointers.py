class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers) - 1

        while l<r:

            sum_l_r = numbers[l] + numbers[r]

            if sum_l_r > target:

                r -= 1
            elif sum_l_r < target :

                l += 1
            
            elif sum_l_r == target:

                return [l+1,r+1]

            else:

                continue
        
        return -1
