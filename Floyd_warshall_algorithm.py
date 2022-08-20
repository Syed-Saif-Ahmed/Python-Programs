
my_list = []
adj_mtx = []

inf = 999999

def min(a,b):
    if a>b:
        return b
    else:
        return a

def floyd_warshall_algo(W):
    n = len(W)
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    D[i][j] = min(D[i][j],D[i][k]+D[k][j])
    return D

def costMatrix(M):
    n = len(M)
    for i in range(n):
        M[i][i] = 0
    for i in range(n):
        for j in range(n):
            if i!=j and M[i][j] == 0:
                M[i][j] = inf
    return M

def graphMakerAjascencyMatrix():
    n = int(input("Enter the number of nodes ::"))
    adj_mtx = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        e = int(input("Enter the node ::"))
        my_list.append(e)
    print("Make the adjascency list ::")
    for row in range(n):
        for col in range(n):
            adj_mtx[row][col] = int(input())
        print()
    print('\n')
    
    for i in adj_mtx:
        print(i)
    print()
    for row in range(n):
        for col in range(n):
            if adj_mtx[row][col] != 0:
                print(my_list[row],"--->",my_list[col])
        print()
    return adj_mtx
def main():
    matrix = graphMakerAjascencyMatrix()
    cost = costMatrix(matrix)
    f = floyd_warshall_algo(cost)
    for i in f:
        print(i)

main()