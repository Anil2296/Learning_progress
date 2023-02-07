age=int(input("Enter age"))
rate=int(input("Enter ticket rate"))
if(age>=60)  :
   concession=100
elif(age>=35):
    concession=0
elif(age>=20):
    concession=20
elif(age>=6) :
    concession=0
elif(age<6)  :
    concession=100
finalrate=rate*(100-concession)/100
print("The final ticket rate and concession for passanger :",finalrate)
print("concession for passanger is :",concession)
