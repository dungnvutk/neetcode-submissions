class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid]>=nums[left] and nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<=nums[left] and nums[mid]<=nums[right]:
                right = mid
            elif nums[mid]>nums[left] and nums[mid]<=nums[right]:
                right = mid
            else:
                return nums[mid]
        return nums[(left+right)//2]
