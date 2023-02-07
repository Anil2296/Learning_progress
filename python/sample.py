list=["omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","alpha","omega","beta"]

mylist=set(list)
#print(mylist)
emlist=[]
for i in mylist:
	count=0
	for j in range(0,len(list)):
		if(i==list[j]):
			count+=1;
	a=(count*100)/len(list)
	if(a>=0.05):
		emlist.append(i);
emlist.sort();
print(emlist);
