class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        l, r = 0, 1
        if len(set(nums[0:k])) == len(nums[0:k]):            
            l, r = 0, k

        while r<len(nums):
            if nums[r] in nums[l:r]:
                for i in range(l,r):
                    if nums[i]==nums[r]:
                        return True
            if r-l>=k:
                l+=1
            r+=1
        return False