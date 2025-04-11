import turtle

turtle.shape('turtle') 

n = int(input(""))

if n < 5 or n > 31 or n % 2 == 0:
    print("Error : n must be an odd number between 5 and 31")
else:
    turtle.speed(0)
    angle = 180 - 180 / n
    
    for _ in range(n):
        turtle.forward(200)
        turtle.right(angle)

turtle.done()
