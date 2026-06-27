class MinStack(object):

    def __init__(self):
        self.values = []
        self.minValue = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.values)>0:
            if value>self.minValue[len(self.minValue)-1]:
                self.minValue.append(self.minValue[len(self.minValue)-1])
            else:
                self.minValue.append(value)
        else:
            self.minValue.append(value)

        self.values.append(value)
        return self

    def pop(self):
        """
        :rtype: None
        """
        self.minValue.pop()
        self.values.pop()
        return self

    def top(self):
        """
        :rtype: int
        """
        return self.values[len(self.values)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minValue[len(self.values)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()