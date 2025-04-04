i = int(input("Enter an integer (0-255): "))
j = int(input("Enter bit position (0-7): "))
print("- partition -")

if i < 0 or i > 255 :
    print("Error : number must be between 0 and 255")

if j < 0 or j > 7 :
    print("Error : numbr must be between 0 and 7")

k = 1
k = k << j

print(f"{i:08b} : binary representation of {i}")
print(f"{k:08b} : bit mask position {j}")
print(f"Is bit of {i} at position {j} on? {i&k>0}")