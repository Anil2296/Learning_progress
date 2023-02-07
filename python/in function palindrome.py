def is_palindrom(s):
    return s[::-1]
s=input()
ans=is_palindrom(s)
if ans==s:
  print("yes")
else:
  print("No")
      
