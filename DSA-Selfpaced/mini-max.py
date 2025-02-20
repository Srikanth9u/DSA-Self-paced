def miniMaxSum(arr):
    # Write your code here
    max_arr=max(arr)
    min_arr=min(arr)
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    print(sum-max_arr,sum-min_arr)
