pt= input("Enter pt: ").upper()
ct= ""
for i in range(len(pt)):
    print(ord(pt[i])-64)
    ct += chr(ord(pt[i]))

print(ct)