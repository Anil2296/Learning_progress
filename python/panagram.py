def pan(input):
    input=input.lower()
    input=set(input)
    ch=0
    k=[]
    for i in input:
        if ord(i) in range(ord('a'), ord('z')+1):
           k.append(i)
    if(len(k)==26):
           return 'true'
    else:
        return 'false'
 

if __name__ == "__main__":
    input = 'The quick brown fox jumps over the lazy dog'
    print (pan(input))
