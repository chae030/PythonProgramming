num1 = int(input("base (16|10|8|2):"))
num2 = int(input("natural number (<128):"), base=num1)

print("----------")
print(f"Hexadecimal:\t{hex(num2)}")
print(f"Decimal:\t{num2}")
print(f"Octal:\t\t{oct(num2)}")
print(f"Binary:\t\t{bin(num2)}")
