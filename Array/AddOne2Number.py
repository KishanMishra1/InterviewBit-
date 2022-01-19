class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        res=[]
        s="".join(str(a) for a in A)
        k=int(s)+1
        for i in str(k):
            res.append(int(i))
        return res
