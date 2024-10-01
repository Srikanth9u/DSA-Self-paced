class Solution:
    def isPrime(self,N):
        # code here
        if N == 1:
            return False
        i=2
        while (i*i<=N):
            if N % i == 0:
                return False
            i=i+1
        return True