n = int(input())
matrix = [[0]*n for i in range(n)]
a=b=c=d = 0
k = 1
for i in range(n):
        for a in range(i,n-i):
            matrix[i][a] = k
            k+=1
        for b in range(i+1,n-i):
            matrix[b][a] = k
            k+=1
        for c in range(b-1,i,-1):
            matrix[b][c] = k
            k+=1
        for d in range(a,i,-1):
            matrix[d][i] = k
            k+=1
print(matrix)

