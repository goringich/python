import math

B = int(input("B: "))
C = int(input("C: "))
ss = int(input("Введите минимальную СС: "))

def pr(x):
    if x>=ss:
        print("A:", A, "; x:", x)

for A in range(1,100):
    dis = B**2-4*A*C
    if dis > 0:
        x1 = (-B + math.sqrt(dis))//(2*A)
        x2 = (-B - math.sqrt(dis))//(2*A)
        
        pr(x1)
        pr(x2)
        
    elif dis == 0:
        x = -B/2*A
        
        pr(x)
    else:
        print("Error", A)
