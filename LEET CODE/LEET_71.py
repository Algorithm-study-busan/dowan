class Solution:
    def simplifyPath(self, path: str) -> str:

    
        stack=[]
        path = path.split("/")
         
        for i in path:
            if(i=="" or i=="."):
                continue
            elif(i==".."):
                if(len(stack)>0):
                    stack.pop()
                    stack.pop()
            else:
                stack.append("/")
                stack.append(i)

        if(len(stack)==0):
            return "/"
   
        
        return "".join(stack)
        