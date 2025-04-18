n = int(input("Enter number of force-distance pairs (1 to 10): "))
print("="*10)

if n < 1 or n > 10 :
    print("Error: Number must be between 1 and 10.")
else :
    print(f'Expected number of force-distance pairs: {n}')
    print("="*10)
    
    forces_N = [0.0] * n
    distances_m = []
    for i in range(n) :
        forces_N[i] = float(input(f"Enter force[{i}] in Newtons: "))
        distances_m.append(float(input(f"Enter distance[{i}] in meters: ")))
    print("="*10)
    
    work_done_J = []
    for i in range(n) :
        work_done_J.append(forces_N[i]*distances_m[i])
    
    print(f"Collected forces (N): {forces_N}")
    print(f"Collected distances (m): {distances_m}") 
    print(f"Calculated work done (J): {work_done_J}")
    print("="*10)
    
    print(f"{'Index':^6}|{'Force(N)':^12}|{'Distance(m)':^12}|{'Work Done(J)':^12}")
    for i in range(n) :
        print(f"{i:6d}|{forces_N[i]:12.2f}|{distances_m[i]:12.2f}|{work_done_J[i]:12.2f}")
    print("="*10)
    
    total_work_done = 0
    for i in work_done_J :
        total_work_done += i
    print(f"Total work done = {total_work_done:.2f} J")
