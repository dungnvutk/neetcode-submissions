class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<=right:
            if nums[int((left+right)/2)]<target:
                left=int((left+right)/2)+1
            elif nums[int((left+right)/2)]>target:
                right = int((left+right)/2)-1
            elif nums[int((left+right)/2)]==target:
                return int((left+right)/2)
        return -1