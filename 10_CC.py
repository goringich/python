n = int(input('n= '))
d = int(input("CC: "))

arr = []
while n > 0:
    a = n%d
    if a > 9:
        arr.append(chr(55+a))
    else:                
        arr.append(a)
    n = n//d

arr.reverse()
for i in range(len(arr)):
    print(arr[i],end='')


