#User function Template for python3

class Solution:
    #You need to complete this function
    def factorial(self,N):
        #Your code here
        fact =1
        for i in range (1,N+1):
            fact = fact*i
        return fact