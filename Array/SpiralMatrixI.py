def spiralOrder(self,A):
        left,right=0,len(A[0])
        top,bottom=0,len(A)
        res=[]
        dir=0
        while left<right and top<bottom:
                if (dir==0):
                    for i in range(left,right):
                        res.append(A[top][i])
                    top+=1
                elif dir==1:
                    for i in range(top,bottom):
                        res.append(A[i][right-1])
                    right-=1
                elif dir==2:
                    for i in range(right-1,left-1,-1):
                        res.append(A[bottom-1][i])
                    bottom-=1
                elif dir==3:
                    for i in range(bottom-1,top-1,-1):
                        res.append(A[i][left])
                    left+=1
                dir=(dir+1)%4
        return res
