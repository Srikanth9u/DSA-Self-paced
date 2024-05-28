class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        #Your code here
        r=B/A
        a= A*pow(r,N-1)
        return a