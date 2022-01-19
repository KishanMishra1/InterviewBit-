def maxSubArray(self, A):
        max=-sys.maxsize-1
        max_tn=0
        for i in range(len(A)):
            max_tn+=A[i]
            if max_tn>max:
                max=max_tn
            if max_tn<0:
                max_tn=0
        return max
