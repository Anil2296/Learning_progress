from collections import Counter
def find_common_characters(msg1,msg2):
   k=Counter(msg1)
   print(k)
   l=Counter(msg2)
   print(l)
   m=k&l
   a=list(m)
   return "".join(a)

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
