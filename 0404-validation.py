k = 1
i = int(input("Enter an integer (0-255):"))
j = int(input("Enter bit position (0-7):"))

if i < 0 or i > 255 :
    print("Error : number must be between 0 and 255")
elif j < 0 or j > 7 :
    print("Error : number must be between 0 and 7")
else :
    print("- partition -")
    k = k << j
    print(f"{i:08b} : binary representation of {i}")
    print(f"{k:08b} : bit mask for position {j}")
    print(f"Is bit of {i} at position {j} on? {i&k>0}")