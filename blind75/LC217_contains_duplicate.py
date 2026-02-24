class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()

        for element in nums:

            if element in hashset:
                return True
            else:
                hashset.add(element)
        return False

        