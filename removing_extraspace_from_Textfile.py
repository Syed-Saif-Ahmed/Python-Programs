def spacecheck(name1,name2):
    f1=open(name1,'r')
    f2=open(name2,'a')
    for line in f1:
        lst=line.split()
        str=""
        for i in lst:
            str=str+i+" "
        str=str+"\n"
        f2.write(str)
    f1.close()
    f2.close()
    print("Successfully copied !")
# main
F1=input("Which File To copy ::")
F2=input("Where To copy ::")
spacecheck(F1,F2)
