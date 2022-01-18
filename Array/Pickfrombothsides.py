def solve(self, A, B):
        maxsum = sum(A[-1*B:])
        if B < len(A):
            tempsum = maxsum
            for i in reversed(range(B+1)):
                tempsum = -A[-i] + tempsum + A[B-i]
                if tempsum > maxsum:
                    maxsum = tempsum

        return maxsum
