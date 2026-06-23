class Solution(object):
    def evalRPN(self, tokens: List[str])->int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        answer = []
        num = 0
        for i in range(len(tokens)):
            # if tokens[i].isalnum():
            #     answer.append(tokens[i])
            if tokens[i]=='+':
                num = int(answer[len(answer)-2])+int(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(num)
            elif tokens[i]=='-':
                num = int(answer[len(answer)-2])-int(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(num)
            elif tokens[i]=='*':
                num = int(answer[len(answer)-2])*int(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(num)
            elif tokens[i]=='/':
                num = int(float(answer[len(answer)-2])/float(answer[-1]))
                answer.pop()
                answer.pop()
                answer.append(num)
            else:
                answer.append(tokens[i])
                
        return int(answer[0])