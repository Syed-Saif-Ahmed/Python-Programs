n=int(input('enter a number >>'))
if n > 0:
    for i in range (2,n):
        rem=n%i
        if rem==0:
            print(n,"is not a prime")
            break
    else:
        print(n,"is a prime")
else:
    print("invalid number !!!")
