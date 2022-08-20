def place(k,i):
    for j in range(1,k):
        if ((x[j] == i)  or (abs(x[j]-i) == abs(j-k) )): #x[k]=i is same column and abs(x[j]-i) == abs(j-k) is same diagonal
            return False
    return True
def NQueen(k,i):
    for i in range(1,n+1):
        if place(k,i):
            x[k] = i
            print(k)
            if (k == n):
                print(x[1:])
            else:
                NQueen(k+1,n)

n = 4
x = [0 for i in range(n+1)]
'''for k in range(1,n+1):
    NQueen(k,n)
 '''
NQueen(1,n)
