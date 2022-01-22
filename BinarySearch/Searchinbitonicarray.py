class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a, B):
        l=0
        h=len(a)-1
        while l<=h:
            mid=(l+h)//2
            if a[mid]==B:
                return mid
            if a[mid-1]<a[mid]<a[mid+1]:
                if a[mid]>B:
                    h=mid-1
                elif a[mid]<B:
                    l=mid+1
            else:
                if a[mid]>B:
                    l=mid+1
                elif a[mid]<B:
                    h=mid-1
