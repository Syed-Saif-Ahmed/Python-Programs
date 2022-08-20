import matplotlib.pyplot as plt
a=[1,15,18,88]
b=['A','B','C','D']
clr=['m','g','y','b']
plt.bar(b,a,color=clr)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("example")
plt.legend(['a','b','c','d'])

plt.show()
