class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        s=a+b
        s=s%(10**9+7)
        return s