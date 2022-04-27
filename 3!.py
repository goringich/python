'''
#3
k = 0
m = 1156
for i in range(1156, 12209+1):
    if (i % 2 == 0 or i % 5 == 0) and (i % 7 > 0 and i % 13 > 0 and i % 17 > 0 and i % 23 > 0):
        k+=1
        m = max(m, 12209)
print(k, m)
#я не знаю) у меня пишет 4726 12209


#4
k = 0
ma = 2568
mi = 7858+1
for i in range(2568, 7858+1):
    if (i % 4 == 0 or i % 5 == 0) and (i % 11 > 0 and i % 20 > 0 and i % 27 > 0):
        k+=1
        mi = min(i, mi)
        ma = max(i, ma)
print(mi, ma)

#5
k = 0
ma = 3672
mi = 9117+1
s = 0
for i in range(3672, 9117+1):
    if i % 3 == 2 and i % 5 == 4:
        k+=1
        s += i
print(k, s)
'''
#5
k = 0
ma = 3439
for i in range(3439, 7410+1):
    if (i % 9 == 0 or i % 10 == 0 or i % 11 == 0) and (i % 2 != i % 6):
        k+=1
        ma = max(i, ma)
print(k, ma)