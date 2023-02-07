a=input("enter gender")
b=int(input("enter the marks"))
c=input("enter name")
d=int(input("enter age"))
if(d>=20):
    if(a=="male"):
     if(b>=80 and d>=28):
        print("The candidate selected") 
     else:
        print("The candidate not selected")

    else:
        if(a=="female"):
            if(b>=60 and d>=30):            
             print("the candidate selected")
            else:
              print("the candidate not selected")
        else: 
           print("the candidate not selected")
else:
    print("not eligible")
    
