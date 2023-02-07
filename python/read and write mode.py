fo=open("renu.txt","r+")
str=fo.read()
po=fo.tell()
p=fo.seek(0, 0)
print("read string is : ",str)
print(" position string is : ",p)
print("seek string is : ",p)
fo.close()  
               
