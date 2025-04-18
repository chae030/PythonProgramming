n = int(input("Enter number of students: "))
print("Number of students: ", n)
print("==========\n")
d = {}

for _ in range(n) :
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    d[id] = name
    
print("="*10)

for key, value in d.items() :
    print(key, " : ", value)
    
print("="*10)

look_up = input("Enter ID to look up: ")
print("="*10)
if look_up in d.keys() :
    print(look_up, " : ", d[look_up])
else :
    print(look_up, " : not found")