str=input("Enter the lower case string:")
i=0
ch=''

while len(str)>i:  #string is being checked 
    if str[i]>='a' and str[i]<='z' :  #must be in a to z range
        ch+=chr(ord(str[i])-32)  #will change it to lowercase
    else:
        ch += chr(ord(str[i]))  #if already capital, not change
    i+=1
print("Lower case string converted", ch)
