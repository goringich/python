'''
sr = []
print("a")
for i in range(1012, 9638+1):
    if i % 3 == 0 and i % 11 > 0 and i % 13 > 0 and i % 17 > 0 and i % 19 > 0: 
        sr.append(i)
maxA = max(sr)
print(len(sr), maxA)
'''


k = 0
m = 1012
for i in range(1012, 9638+1):
    if i % 3 == 0 and i % 11 > 0 and i % 13 > 0 and i % 17 > 0 and i % 19 > 0: 
        k+=1
        m = max(m, i)
print(k, m)

    
