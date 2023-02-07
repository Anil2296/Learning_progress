from collections import Counter
def max_frequency_word_counter(data):
    l=data.split()
    word=""
    k=0
    m=0
    frequency=0
    h=Counter(l)
    k=[]
    v=[]
    a=list(h.keys())
    print(a)
    b=list(h.values())
    
    c=max(b)
    e=b.index(c)
    s=a[e]
    d=b.count(c)
    if(d==1):
        print(s,c)
    else:
        max1=0
        for i in range(0,len(b)):
            if b[i]==c:
                k=len(a[i])
                if(max1<k):
                    max1=k
                    ans=i
                    
        
        print(c,a[ans])             
                      
                 
                      
                 
                 
            
        
    
    
    
    
                
    
    
   


    
    



data="data-Hands to clap and eyes to see"
max_frequency_word_counter(data)
