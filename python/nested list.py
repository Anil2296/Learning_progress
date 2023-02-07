name=["anil","kumar","sai","siva"]
score=[34.5,56.7,34.5,67.9]
list=[]
for i in name:
    print(i)
for j in score:
      print(j)  
list.append(name)
name.append(score)
n=len(list)
for i in range(0,n):
    if(list[i][1]==list[i+1][1]):
        print(list[i][0])
        
