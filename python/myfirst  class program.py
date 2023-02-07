class mobile:
    def __init__(self,company,cost):
        self.company=company
        self.cost=cost
    def display(self):
        print("the company :",self.company)
        print("the cost:",self.cost)
        print("\n")
class features(mobile):
    def __init__(self,company,cost,ram,memory):
       mobile.__init__(self,company,cost)
       self.ram=ram
       self.memory=memory
    def disp1(self):
        print("the company :",self.company)
        print("the cost:",self.cost)
        print("the ram:",self.ram)
        print("the memory:",self.memory)
        print("\n")
class camera(features):
    def __init__(self,company,cost,ram,memory,cam):
        features.__init__(self,company,cost,ram,memory)
        self.cam=cam
    def disp2(self):
        print("the company :",self.company)
        print("the cost:",self.cost)
        print("the ram:",self.ram)
        print("the memory:",self.memory)
        print("the camera is:",self.cam)
        print("\n")
class battery(mobile):
    def __init__(self,company,cost,batt):
        mobile.__init__(self,company,cost)
        self.batt=batt
    def dip3(self):
        print("the company :",self.company)
        print("the cost:",self.cost)
        print("battery:",self.batt)
        print("\n")
print("!!!!....MOBILE DETAILS.............!!!!")
print("!!!!..1..All details of mobile.....!!!!")
print("!!!!..2.mobile Ram and Rom.........!!!!")
print("!!!!..3.mobile company and cost....!!!!")
print("!!!!..4.the battery capacity.......!!!!")
while(1):
    p=int(input("enter the choice:"))
    if(p==1):
       print("!!!All details of mobile.....!!!")
       s1=camera("Apple",100000,"6gb","64gb","200pixel")
       s1.disp2()
    elif(p==2):
       print("!!!mobile Ram and Rom....!!!")
       s2=features("Apple",100000,"6gb","64gb")
       s2.disp1()
    elif(p==3):
       print("!!!mobile company and cost....!!!")
       s3=mobile("APPle",100000)
       s3.display()
    elif(p==4):
      print("!!!the battery capacity!!!")
      s4=battery("APPLE",100000,"2hrs")
      s4.dip3()



        
        
