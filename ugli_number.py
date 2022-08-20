def sumofdigits(n):
    """This code will return the sum of
        digits of the number"""
    s=0
    while n>0:
        d=n%10
        s=s+d
        n=n//10
    return s
#__main__
x=int(input("Enter the number ::"))
sum=sumofdigits(x)
while sum>=1:
    if sum==1:
        print(x,"is an ugli number ")
        break
    elif sum>1 and sum<10:
        print(x,"is not a ugli number")
        break
    sum=sumofdigits(sum)


