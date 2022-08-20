T=eval(input("Enter a tuple >>>"))
len=len(T)
max=smax=T[0]
for i in range(len):
    if T[i] > max:
        max=T[i]
for j in range(len):
    if T[j] > smax and T[j]< max:
        smax=T[j]
print("second largest no. is",smax)
