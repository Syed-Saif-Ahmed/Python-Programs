def count(n):
    c=0
    while n>0:
        n=n//10
        c+=1
    return c
def isarmstrong(x):
    s=rev=0
    while x>0:
        r=x%10
        s+=r**co
        x=x//10
    return s
ll=int(input("enter lower ::"))
ul=int(input("enter upper ::"))
for i in range (ll,ul+1):
    co=count(i)
    if isarmstrong(i)== i:
        print(i,end=",")
else:
    print("none")
