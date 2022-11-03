class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_ans = [ sum(nums[:i+1]) for i in range(len(nums))]
        
        return list_ans
