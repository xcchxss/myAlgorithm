n, m = map(int, input().split())

res = [[0 for j in range(m)]for i in range(n)]

dx = [-1,0,1,0]   
dy = [0,1,0,-1]    

x,y,d = 0,0,1

for i in range(1,n*m+1):
    res[x][y] = i
    a,b = x+dx[d],y+dy[d]
    if a<0 or a>=n or b<0 or b>=m or res[a][b]:
        d  = (d+1)%4
        a,b = x+dx[d],y+dy[d]
    x,y = a,b

for i in range(n):
    for j in range(m):
        print(res[i][j],end = ' ')
    print()