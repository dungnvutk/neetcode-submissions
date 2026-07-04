class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2)<len(s1):
            return False
        s1sorted = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            window = s2[i:(i+len(s1))]
            if sorted(window)==s1sorted:
                return True
        return False