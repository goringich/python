m = 2807
s = 0
for i in range(2807, 8558+1):
    if i % 2 == 1 and i // 2 % 2 == 1 and i % 9 == 5:
        m = max(m, i)
        s += i
print(m, s)
        
    
