try:
    fileptr=open("anil.py","w")
    try:
        fileptr.write("Hi")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")
