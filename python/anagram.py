from collections import Counter

def a(l1,l2):
    if(Counter(l1)==Counter(l2)):
        print("anagrams")
    else:
        print("not anagrams")


while(1):
  l1=input()
  l2=input()
  a(l1,l2)
