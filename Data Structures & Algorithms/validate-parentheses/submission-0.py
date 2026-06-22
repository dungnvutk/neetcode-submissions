class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        stack = []
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            if s[i]==')':
                if len(stack)==0:
                    return False
                if stack[len(stack)-1] !='(':
                    return False
                else:
                    stack.pop()
            if s[i]=='[':
                stack.append(s[i])
            if s[i]==']':
                if len(stack)==0:
                    return False
                if stack[len(stack)-1] !='[':
                    return False
                else:
                    stack.pop()
            if s[i]=='{':
                stack.append(s[i])
            if s[i]=='}':
                if len(stack)==0:
                    return False
                if stack[len(stack)-1] !='{':
                    return False
                else:
                    stack.pop()
        if stack==[]:
            return True
        else:
            return False
