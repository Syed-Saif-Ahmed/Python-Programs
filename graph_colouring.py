def graphColour(k):
    for c in range(1,m+1):
        if (isSafe(k,c)):
            x[k] = c
            if ((k+1)<n):
                graphColour(k+1)
            else:
                print(x)
                return
def isSafe(k,c):
    for i in range(n):
        if (G[k][i] == 1 and c == x[i]):
            return False 
    return True


n = 4 #vertices
m = 3 #colour
#v = ['A','B','C','D']
G = [[0,1,0,1],[1,0,1,1],[0,1,0,1],[1,1,1,0]]
x = [0,0,0,0]
graphColour(0)