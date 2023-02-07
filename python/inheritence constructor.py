class student(object):
    def __init__(self,name,id,branch):
        self.name=name
        self.id=id
        self.branch=branch
    def disp(self):
        print("name=",self.name)
        print("id=",self.id)
        print("branch=",self.branch)
class child(student):
    def __init__(self,name,id,branch,m1,m2,m3):
        student.__init__(self,name,id,branch)
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def process(self):
        self.tot=self.m1+self.m2+self.m3
        self.avg=self.tot/3
        if(self.avg>80):
            ans="grade A"
        elif(self.avg>60):
            ans="grade B"
        else:
            ans="Work hard"
        print(ans)
    def disp(self):
        print("name=",self.name)
        print("id=",self.id)
        print("branch=",self.branch)
        print("total=",self.tot)
        print("avg=",self.avg)
        #print('ans=',self.ans)
s1=student("anil",1243,"IT")
s2=child("anil",1243,"IT",100,90,90)
while(1):
    ch=int(input("Enter choice"))
    if(ch==1):
        s1.disp()
    else:
        s2.process()
        s2.disp()
        
'''
s2.process()
s2.disp()'''

