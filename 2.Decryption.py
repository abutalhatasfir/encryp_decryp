ct = str(input("Enter the Ciphertext: ").upper()).replace(" ", "")
key= input("Enter the key: ")
pt = ""
if key.isdigit():
  
    key = int(key)
    if key > 26:
        key = key % 26

    for i in range(len(ct)):

        ci = ord(ct[i]) - 64
        pi = ci - key
        
        if pi >26:
            pi = pi % 26
        elif pi <= 0:
            pi += 26

        pt += chr(pi+64)
  
    print(f"The Plaintext: {pt}")

elif key.isalpha():

    key = key.upper()

    for i in range(len(ct)):

        ki = ord(key[i%len(key)]) - 64
        ci = ord(ct[i]) - 64
        pi = ci - ki

        if pi >26:
            pi = pi % 26
        elif pi <= 0:
            pi += 26

        pt += chr(pi+64)
  
    print(f"The Plaintext: {pt}")

else:
    print("Invalid key")