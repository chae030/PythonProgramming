i = int(input("Enter an integer (0-255): "))
j = int(input("Enter bit position (0-7): "))
print("----------")

print(f"{i:08b} : binary representation of {i}")
k = 1
k = k << j
print(f"{k:08b} : bit mask for position {j}")
print(f"Is bit of {i} at position {j} on? {i & k > 0}")