var1= input("Enter the string: ")

s1= var1.find('not') # not er staring index number khuje ber kore 
s2= var1.find('poor') # poor er staring index show ney 

if s1<s2 and s1>0 and s2>0:
    #.replace(old string , new string,count)
    new_var= var1.replace(var1[s1:(s2+4)],'good') 
    print(new_var)
else:
    print(var1)