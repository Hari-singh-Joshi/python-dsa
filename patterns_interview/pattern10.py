ch="A"
for i in range(0,4):
    for j in range(0,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)
    print("")
        