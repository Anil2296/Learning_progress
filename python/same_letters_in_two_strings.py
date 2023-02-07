def find_common_characters(msg1,msg2):
    list=[]
    for x in msg1:
        print(x)
        if x==" ":
            continue
        else:
            for y in msg2:
                print(y)
                if x == " ":
                    continue
                elif x == y:
                    if x in list:
                        print("equal to string",x)
                        break
                    else:
                        list.append(x)
                        break
    output="".join(list)
    if len(output)==0:
        return -1
    else:
        return output

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
