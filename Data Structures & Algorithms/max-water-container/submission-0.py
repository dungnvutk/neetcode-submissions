class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = (len(height)-1)*min(height[0],height[len(height)-1])
        for p1 in range(len(height)):
            p2 = len(height)
            while p1<p2:
                p2=p2-1
                newVolume = (p2-p1)*min(height[p1],height[p2])
                if volume < newVolume:
                    volume = newVolume
                while p1<p2 and height[p2]==height[p2-1]:
                    p2=p2-1
        return volume