def max(a,b):
    if a>b:
        return a
    return b
def main():
    p1 = eval(input("Enter the profit list ::"))
    w1 = eval(input("Enter the corresponding rod ::"))
    m1 = int(input("capasity of the bag ::"))
    n1 = int(input("Enter the number of items ::"))

    p = [0]+p1
    wt = [0]+w1
    m = m1
    n = n1
    #p = [0,100,20,60,40]
    #wt = [0,3,2,4,1]
    #m = 5
    #n = 4
    k = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(0,n+1,1):
        for w in range(0,m+1,1):
            if (i == 0 or w == 0):
                k[i][w] = 0
            elif (wt[i]<=w):
                k[i][w] = max(k[i-1][w],p[i]+k[i-1][w-wt[i]])
            else:
                k[i][w] = k[i-1][w]
    for i in k:
        print(i)
    i = n+1
    w = m+1
    mark = [0 for i in range(len(p))]
    while i>0 and w>0:
        if k[i][w] != k[i-1][w]:
            mark[i] = 1
            w = w-wt[i]
            i-=1
        else:
            i-=1
    print()
    mark.pop(0)
    print(mark)
main()
