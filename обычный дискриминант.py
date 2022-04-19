import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

dis = B**2-4*A*C
if dis > 0:
    x1 = (-B + math.sqrt(dis))/(2*A)
    x2 = (-B - math.sqrt(dis))/(2*A)
    
    print(x1)
    print(x2)
    
elif dis == 0:
    x = -B/2*A
    
    print(x)
else:
    print("Ошибка, дискриминант =", dis)

