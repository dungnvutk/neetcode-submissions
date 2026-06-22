class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        water = 0

        maxLeft[0]=0
        # for i in range(0,len(height)-1):
        #     if height[i]>maxLeft[i]:
        #         maxLeft[i+1]=height[i]
        #     else:
        #         maxLeft[i+1]=maxLeft[i]
        
        maxRight[-1]=0
        # for i in range(2,len(height)+1):
        #     j=len(height)-i
        #     if height[j]>maxRight[j]:
        #         maxRight[j]=height[j]
        #     else:
        #         maxRight[j]=maxRight[j+1]
        
        current_max = 0
        for i in range(n):
            maxLeft[i] = current_max
            current_max = max(current_max, height[i])

        # Pre-populate maxRight from right to left
        current_max = 0
        for i in range(n - 1, -1, -1):
            maxRight[i] = current_max
            current_max = max(current_max, height[i])
        maxLeft[0]=0
        maxRight[-1]=0

        for i in range(len(height)):
            water += max(min(maxRight[i],maxLeft[i])-height[i],0)
        return water
        