l=eval(input("enter 10 integers ::"))
len=len(l)
for i in range(0,len):
    for j in range (i+1,len+3):
        if l[i]==l[j]:
            del l[j]
            continue
        del l[i]
print("modified list is :",l)
