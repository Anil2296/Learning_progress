vowels=['a','e','i','o','u']

def encrypt_sentence(sentence):
    final=[]
    list_sentence = sentence.split(" ")
    for index,word in enumerate(list_sentence):
        print(index)
        if (index+1)%2!=0:
            final.append(word[::-1])
        else:
            v=[]#to store all vowels
            t=[]#to store the letters temporily
            for letter in word:
                if letter not in vowels:
                    t.append(letter)
                    print(t)
                else:
                    v.append(letter)
                    print(v)
            t.extend(v)
            print(t)
            final.append("".join(t))
            print(final)
    
    return " ".join(final)
                    
sentence="hello i am omkar"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
