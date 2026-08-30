pt = str(input("Enter the Plaintext: ").upper().split())
key= input("Enter the key: ")
ct = ""
if key.isdigit():
  
    key = int(key)
    if key > 26:
        key = key % 26

    for i in range(len(pt)):

        pi = ord(pt[i]) - 64
        ci = pi + key
        if ci >26:
            ci = ci % 26
        elif ci <= 0:
            ci += 26
        

        ct += chr(ci+64)
  
    print(f"The Ciphertext: {ct}")

elif key.isalpha():

    key = key.upper()

    for i in range(len(pt)):

        ki = ord(key[i%len(key)]) - 64
        pi = ord(pt[i]) - 64
        ci = pi + ki

        if ci >26:
            ci = ci % 26
        elif ci <= 0:
            ci += 26

        ct += chr(ci+64)
  
    print(f"The Ciphertext: {ct}")

else:
    print("Invalid key")