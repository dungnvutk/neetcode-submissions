class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0,len(nums)-1
        while l<=r:
            if nums[l]==val:
                if nums[r]!=val:
                    temp=nums[l]
                    nums[l]=nums[r]
                    nums[r]=temp
                else:
                    r-=1
            else:
                l+=1
        return l