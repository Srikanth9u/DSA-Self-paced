def diagonalDifference(arr):
    # Write your code here
    l=len(arr)
    lsum=0
    rsum=0
    for i in range(l):
        lsum=lsum+arr[i][i]
        rsum=rsum+arr[i][l-i-1]
    diff=rsum-lsum
    
    return abs(diff)
