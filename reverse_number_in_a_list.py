l=eval(input("enter some numbers in alist:"))
for i in range (0,len(l)):
    rev=0
    x=l[i]
    while x>0:
        r=x%10
        rev=rev*10+r
        x=x//10
        l[i]=rev
print("modefied list is :",l)
