class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        while left<right:
            mid = (left+right)//2
            hour = 0
            for i in range(len(piles)):
                hour += (piles[i]+mid-1)//mid
            if hour > h:
                left = mid+1
            elif hour<=h:
                right=mid
        return right