pt= input("Enter the Plaintext: ").upper()
ki= int(input("Enter key: "))
ct= ""
if ki > 26:
    ki = ki % 26
for i in range(len(pt)):
    pi = ord(pt[i]) - 64
    ci = pi + ki
    if ci >26:
        ci = ci % 26
    ct += chr(ci+64)

print(f"The Chipertext: {ct}")

