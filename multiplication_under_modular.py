#User function Template for python3

class Solution:
    def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''   
        # code here
        m=a*b
        m=m%(10**9+7)
        
        return int(m)