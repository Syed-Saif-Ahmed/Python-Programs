L=eval(input("Enter the numbers >>> "))
sum=0
length=len(L)
for i in range (0,length,1):
    sum=sum+L[i]
ave=sum/length
print("Sum of the numbers >>>",sum)
print("ararge of the numbers >>>",ave)
