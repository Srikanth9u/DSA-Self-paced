def lonelyinteger(a):
    # Write your code here
    a.sort()
    l=len(a)
    if l==1:
        return 1
    else:
        for i in range(0,l-1,2):
            if a[i]!=a[i+1]:
                return a[i]
            return a[-1]
