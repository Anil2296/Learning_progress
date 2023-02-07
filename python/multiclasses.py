class student:
    def __init__(self,id,name,branch):
        self.id=id
        self.name=name
        self.branch=branch
    def display(self):
        print("the id is:",self.id)
        print("the name:",self.name)
        print(" the branch:",self.branch)
class year(student):
    def __init__(self,id,name,branch,currentyear,birthyear):
        student.__init__(self,id,name,branch)
        self.currentyear=currentyear
        self.birthyear=birthyear
    def display1(self):
        print("the id is:",self.id)
        print("the name:",self.name)
        print(" the branch:",self.branch)
        print("current year is :",self.currentyear)
        print("birth year :",self.birthyear)
class age(year):
    def __init__(self,id,name,branch,currentyear,birthyear,years):
        year.__init__(self,id,name,branch,currentyear,birthyear)
        self.years=years
    def display2(self):    
        print("the id is:",self.id)
        print("the name:",self.name)
        print(" the branch:",self.branch)
        print("current year is :",self.currentyear)
        print("birth year is:",self.birthyear)
        print("age is :",self.years)
'''s1=student(1243,"Anil","IT")
s1.display()'''
s2=year(1243,"Anil","IT",2022,2002)
s2.diplay1()
years=currentyear-birthyear
s3=age(1243,"Anil","IT",2022,2002,years)
s3.display2()












        
