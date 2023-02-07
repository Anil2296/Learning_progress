def sample():
    f1=open("filename.txt","r")
    r=f1.read()
    f2=open("kumar.txt","r")
    s=f2.read()
    f3=open("renuka.txt","w")
    f3.write(r)
    f3.write(s)
    f3.close()
sample()
    
