def coverPoints(self, A, B):
        x,y=A[0],B[0]
        total=0
        for i,j in zip(A,B):
            dx,dy=abs(i-x),abs(j-y)
            if dx>dy:
                total+=dx
            else:
                total+=dy
            x,y=i,j
        return total
