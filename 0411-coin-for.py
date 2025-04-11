coin = int(input())
c = [500, 100, 50, 10, 5, 1]

print("- partition -")

if coin < 0:
    print("Error : Invalid input. Please enter a non-negative integer.")
else:
    for i in c:
        count = coin // i
        coin %= i
        print(f'{i}: {count}')