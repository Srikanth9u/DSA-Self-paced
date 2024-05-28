#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        if N == 0 or N ==1:
            return 1
        log_sum = 0
        for i in range(1, N+1):
            log_sum += math.log10(i)
        return math.floor(log_sum + 1)
        
        

