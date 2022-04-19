import math

B = int(input("B: "))
C = int(input("C: "))

def pr(x):
    print("A:", A, "; x:", x, "; dis:", dis)

for A in range(1,5):
    dis = B**2-4*A*C
    if dis > 0:
        x1 = (-B + math.sqrt(dis))/(2*A)
        x2 = (-B - math.sqrt(dis))/(2*A)
        
        if (x1 % 10) != 0:
            pass
        elif (x2 % 10) != 0:
            pass
#             x1=x1/10-x1%10
#             x2=x2/10-x2%10
#             pr(x1)
#             pr(x2)
        else:
            pr(x1)
            pr(x2)
        
    elif dis == 0:
        x = -B/2*A
        
        pr(x)
    else:
        print("Error", A)
