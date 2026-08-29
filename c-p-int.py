ct= input("Enter the Ciphertext: ").upper()
ki= int(input("Enter key: "))
pt= ""
if ki > 26:
    ki = ki % 26
for i in range(len(ct)):
    ci = ord(ct[i]) - 64
    pi = ci - ki
    if pi >26:
        pi = pi % 26
    elif pi <= 0:
        pi += 26
    pt += chr(pi+64)

print(f"The Plaintext: {pt}")
