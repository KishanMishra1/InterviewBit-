class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        sumofall=sum(A)
        n=len(A)

        total= (n*(n+1)//2- n)
        return sumofall-total
