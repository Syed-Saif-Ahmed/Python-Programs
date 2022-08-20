
p = [4,10,3,12,20,7]
def mco(p):
    n = len(p)
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    
    for l in range(1,n-1):
        for i in range(1,n-l):
            j = i+l
            m[i][j] = 999999
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    for i in range(1,n-1):
        print(m[i])
    print('\n')
    for i in range(1,n-1):
        print(s[i])
    print('\n')
    return m[1][n-1]
print(mco(p))
