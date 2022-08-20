import matplotlib.pyplot as plt

n=int(input("No.of datas:"))
mon=input("month:")
l1=[]
l2=[]
for i in range(n):
    mod=input("Enter model:")
    val=float(input("Enter sale :"))
    l1.append(mod)
    l2.append(val)

plt.bar(l1,l2)
plt.xlabel(mod)
plt.ylabel('sale done')
plt.show()

    
