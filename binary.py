n=int(input("enter the number ::"))
b=''
while n>=1:
    if n%2!=0:
        b+='1'
    else:
        b+='0'
    n=n//2
print(b[::-1])
