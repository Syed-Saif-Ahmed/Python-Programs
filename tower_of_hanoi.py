def TOH(n,s,a,d):
    if (n==1):
        print(s,"-->",d)
    else:
        TOH(n-1,s,d,a)
        print(s,"-->",d)
        TOH(n-1,a,s,d)
def main():
    n = int(input("Enter the number of disc ::"))
    TOH(n,'A','B','C')
main()