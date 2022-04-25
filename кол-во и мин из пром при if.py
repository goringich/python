'''

for i in range(1000, 9999+1):
    s = 0
    k = 0
    a1 = 11
    a2 = 13
    while i > 0:
        a //= 5
        if k >= 6 and (s % 5 ** 2 == a1 or s % 5 ** 2 == a1):
            k += 1
        a 
print(k)
'''
k = 0
m = 10000
for i in range(1000, 9999+1):
    n = 0
    i1 = i
    while i1 > 0:
        n += 1
        i1 //= 5
    if n >= 6 and (i % 5 ** 2 == 13 or i % 5 ** 2 == 11):
        k += 1
        m = min(m, i)
    
print(k, m)
