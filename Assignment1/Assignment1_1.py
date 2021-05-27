s= input("Enter the string: ")
if len(s)>2:
    print(s[0:2]+ s[-2:])
else:
    print("Empty string")