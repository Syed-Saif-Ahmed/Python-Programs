def isuptocount(name):
    f=open(name,'r')
    cis=cup=cto=0
    file_line=f.readlines()
    for l in file_line:
        l1=l.split()
        for i in range(0,len(l1)):
            if l1[i]=="is":
                cis+=1
            elif l1[i]=="to":
                cto+=1
            elif l1[i]=="up":
                cup+=1
    f.close()
    return cis,cto,cup
def main():
    n="C:\\Users\\USER\\Desktop\\message.txt"
    isc,toc,upc=isuptocount(n)
    print("no. of is ::",isc,"no. of to ::",toc,"no. of up ::",upc)
#__main__
main()

    
