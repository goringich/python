d = int(input('CC: '))
n1 = input('n= ')
n = list(n1)    # преобразование строки в список символов
k = 0
R = 0
pr = 0
n.reverse()
for i in range(len(n)):
    if n[i] > '9':
        a = ord(n[i]) - 55
    else:
        a = ord(n[i]) - 48
   
    if a >= d:
        print('ошибка')
        pr = 1
        break
    R = R + a * d**k
    k = k + 1

if pr == 0:
    print(R)

    
