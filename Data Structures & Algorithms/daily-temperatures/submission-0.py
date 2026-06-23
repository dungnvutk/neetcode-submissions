class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [0]
        for i in range(1,len(temperatures)):
            for j in range(len(stack)):
                if stack[j]==0:
                    if temperatures[i]>temperatures[j]:
                        stack[j]=i-j
            stack.append(0)
        return stack