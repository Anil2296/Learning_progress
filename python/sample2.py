customers=['b','b','a','b','z','a']
dic={}
n=len(customers)
for i in customers:
    if i not in dic:
        dic[i]=1
        print(dic[i])
    else:
        dic[i]+=1
        print(dic[i])
ans=[]
for i in dic:
    a=(dic[i]*100)/n
    if(a>=5):
        ans.append(i)
ans.sort()
print(ans)
