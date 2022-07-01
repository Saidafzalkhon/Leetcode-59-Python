n = int(input())
nums = [[0]*n for i in range(n)]
if n != 1:
    a=b=c=d,k = 0,1
    for i in range(n):
        for a in range(i,n-i):
            nums[i][a] = k
            k+=1
        for b in range(i+1,n-i):
            nums[b][a] = k
            k+=1
        for c in range(b-1,i,-1):
            nums[b][c] = k
            k+=1
        for d in range(a,i,-1):
            nums[d][i] = k
            k+=1
    print(nums)
else: print([[1]])