k=0
while(k<3):
 i=input(" please enter gmail .....")
 f='@'
 p=i.count(f)
 c=i.find(f)
 k+=1
 if(p==1 and c>3):
    print("succesfully entered your gmail ")
    print("Thank you")
    print(" ")
 else:
  print("invalid !! please enter proper gmail")
  print(" ")



                   
